from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from controllers.carrier_controllers.setDryingIntervalController import SetDryingIntervalController
from controllers.carrier_controllers.startDryingController import StartDryingController


class AddToDryerForm(Popup):
    item_data_template = DictProperty({})

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
        new_item_data_template['moisture_level'] = self.ids.moisture_level.text
        new_item_data_template['hours_greater_or_less_than_72'] = self.ids.hours_greater_or_less_than_72.text
        new_item_data_template['drying_interval'] = self.ids.drying_interval.text
        return start_drying.main(new_item_data_template)


    def submit_data(self):
        thickness_level = self.ids.thickness_leve.value
        moisture_level = self.ids.moisture_level.value
        hours_greater_or_less_than_72 = self.ids.hours_greater_or_less_than_72.value
        drying_interval = self.ids.drying_interval.value

    def update_new_item_data_template(self, new_item_data_template):
        new_item_data_template['part_thickness'] = self.ids.thickness_level.text
        new_item_data_template['moisture_level'] = self.ids.moisture_level.text
        new_item_data_template['hours_greater_or_less_than_72'] = self.ids.hours_greater_or_less_than_72.text
        new_item_data_template['drying_interval'] = self.ids.drying_interval.text
