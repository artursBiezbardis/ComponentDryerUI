from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from controllers.setDryingTimeController import SetDryingTimeController


class AddToDryerForm(Popup):
    item_data_template = DictProperty({})

    def __int__(self, **kwargs):
        super(AddToDryerForm, self).__init__(**kwargs)

    def set_time_to_dry(self):

        self.ids.drying_interval.value = SetDryingTimeController().main(self.ids.thickness_level.text,
                                                                        self.ids.moisture_level.text,
                                                                        self.ids.hours_greater_or_less_than_72.text,
                                                                        )


    def submit_data(self):
        thickness_level = self.ids.thickness_leve.value
        moisture_level = self.ids.moisture_level.value
        hours_greater_or_less_than_72 = self.ids.hours_greater_or_less_than_72.value
        drying_interval = self.ids.drying_interval.value
