from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from controllers.carrier_controllers.setDryingIntervalController import SetDryingIntervalController
from controllers.carrier_controllers.startDryingController import StartDryingController
from controllers.msl_form_controllers.mslSelectionValuesController import MslSelectionValueController
from view.layouts.numPadPopup import NumPadPopup
from kivy.properties import ObjectProperty


class AddToDryerForm(Popup):
    item_data_template = DictProperty({})
    main_layout = ObjectProperty(None)

    def __int__(self, **kwargs):
        super(AddToDryerForm, self).__init__(**kwargs)
        self.main_layout.ids.scanner_input.readonly = True
        self.main_layout.ids.scanner_input.focus = False
        self.ids.submit_interval.focus = True
        self.main_layout.self.add_carrier['add_status'] = False

    def set_time_to_dry(self):
        if self.spinners_selected():
            self.ids.drying_interval.text = str(SetDryingIntervalController().main(self.ids.thickness_level.text,
                                                                                   self.ids.moisture_level.text,
                                                                                   self.ids.hours_greater_or_less_than_72.text))
            self.ids.submit_interval.disabled = False

    def spinners_selected(self) -> bool:
        result = False
        drying_parameters = [self.ids.thickness_level.text,
                             self.ids.moisture_level.text,
                             self.ids.hours_greater_or_less_than_72.text]
        select = 'Select'
        custom = 'custom'

        if select not in drying_parameters:
            result = True
        if custom in drying_parameters:
            result = False
        return result

    def start_drying(self):
        new_item_data_template = {}
        start_drying = StartDryingController()
        for key, item in self.item_data_template.items():
            new_item_data_template[key] = item
        new_item_data_template['part_thickness'] = self.ids.thickness_level.text
        new_item_data_template['msl'] = self.ids.moisture_level.text
        new_item_data_template[self.create_snake_case_text()] = True
        new_item_data_template['drying_start_interval'] = self.ids.drying_interval.text
        return start_drying.main(new_item_data_template)

    def refresh_main_layout(self):
        self.main_layout.on_dismiss_refresh_main()

    def update_new_item_data_template(self, new_item_data_template):
        new_item_data_template['part_thickness'] = self.ids.thickness_level.text
        new_item_data_template['moisture_level'] = self.ids.moisture_level.text
        new_item_data_template['hours_greater_or_less_than_72'] = self.ids.hours_greater_or_less_than_72.text
        new_item_data_template['drying_interval'] = self.ids.drying_interval.text
        self.main_layout.ids.scanner_input.readonly = False

    def create_snake_case_text(self):

        new_text = self.ids.hours_greater_or_less_than_72.text.replace(' ', '_')

        return new_text

    def update_msl_selection_values(self, thickness):
        values = MslSelectionValueController().main(thickness)
        if values and values[0] == 'custom' and len(values) == 1:
            self.ids.thickness_level.text = values[0]
            self.ids.moisture_level.text = values[0]
            self.ids.hours_greater_or_less_than_72.text = values[0]
            self.ids.hours_greater_or_less_than_72.value = values[0]
            self.ids.drying_interval.text = ''

        else:
            self.ids.moisture_level.values = values

    def open_num_pad(self):
        num_pad = NumPadPopup(layout_for_num_pad=self, auto_dismiss=False)
        num_pad.open()

    def enter_num_pad_text(self, num_pad_instance):
        self.ids.drying_interval.text = num_pad_instance.text

    def disable_spinners(self):
        if self.ids.thickness_level.text == 'custom':
            self.ids.moisture_level.disabled = True
            self.ids.hours_greater_or_less_than_72.disabled = True
            self.ids.drying_interval.disabled = False
        else:
            self.ids.moisture_level.disabled = False
            if self.ids.hours_greater_or_less_than_72.text != 'Select':
                self.ids.hours_greater_or_less_than_72.disabled = False
            self.ids.drying_interval.disabled = True

    def reset_condition_spinner(self):
        self.ids.hours_greater_or_less_than_72.text = 'Select'
        self.ids.submit_interval.disabled = True

    def reset_thickness_spinner(self):
        self.ids.thickness_level.text = 'Select'
        self.ids.submit_interval.disabled = True

    def reset_msl_spinner(self):
        self.ids.moisture_level.text = 'Select'
        self.ids.submit_interval.disabled = True

    def enable_submit(self):
        self.ids.submit_interval.disabled = False
