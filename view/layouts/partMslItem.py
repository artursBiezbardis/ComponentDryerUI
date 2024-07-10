from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, DictProperty


class PartMslItem(BoxLayout):
    item = DictProperty({})
    add_to_dryer_form = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item['hours_grater_or_less'] = self.get_hours_grater_or_less()
        self.item['drying_start_interval'] = self.convert_drying_interval_to_hours(self.item['drying_start_interval'])

    def set_to_form(self):
        self.add_to_dryer_form.set_form_from_list(self.item)

    def get_hours_grater_or_less(self):

        if self.item['hours_greater_than_72']:
            return 'hours greater than 72'
        elif self.item['hours_less_then_72']:
            return 'hours greater than 72'
        else:
            return 'custom'

    def get_thickness(self):
        return self.item['thickness']

    def get_msl(self):
        return self.item['msl']

    def get_drying_start_interval(self):
        return str(self.convert_drying_interval_to_hours(self.item['drying_start_interval']))

    @staticmethod
    def convert_drying_interval_to_hours(drying_interval_sec):
        hours = drying_interval_sec / 3600

        return hours


