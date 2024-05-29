from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from controllers.carrier_controllers.setDryingIntervalController import SetDryingIntervalController
from controllers.carrier_controllers.startDryingController import StartDryingController
from controllers.msl_form_controllers.mslSelectionValuesController import MslSelectionValueController
from kivy.properties import ObjectProperty



class AddToDryerForm(Popup):
    item_data_template = DictProperty({})
    main_layout = ObjectProperty(None)

    def __int__(self, **kwargs):
        super(AddToDryerForm, self).__init__(**kwargs)

    def set_time_to_dry(self):
        self.ids.drying_interval.text = str(SetDryingIntervalController().main(self.ids.thickness_level.text,
                                                                               self.ids.moisture_level.text,
                                                                               self.ids.hours_greater_or_less_than_72.text))

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

    def create_snake_case_text(self):

        new_text = self.ids.hours_greater_or_less_than_72.text.replace(' ', '_')

        return new_text

    def update_msl_selection_values(self, thickness):
        values = MslSelectionValueController().main(thickness)
        if values[0] == 'custom' and len(values) == 1:
            self.ids.thickness_level.text = values[0]
            self.ids.moisture_level.text = values[0]
            self.ids.hours_greater_or_less_than_72.text = values[0]
            self.ids.hours_greater_or_less_than_72.value = values[0]
            self.ids.drying_interval.text = ''
            self.ids.drying_interval.disabled = False

        else:
            self.ids.moisture_level.values = values