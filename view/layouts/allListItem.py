from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty, ObjectProperty
from datetime import datetime
from utilities.timer_utils import TimerUtilities


class AllListItem(BoxLayout):
    item = DictProperty({})
    add_to_dryer_form = ObjectProperty(None)
    parent_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dt_format = "%Y-%m-%d %H:%M:%S.%f"

    def set_list_item_color(self):
        result = TimerUtilities().time_left(self.item)
        if result <= 0 and self.item['in_dryer']:
            self.parent_layout.all_items_collection[self.item['carrier_barcode']]['status'] = 'green'
            return eval('0.34, 0.59, 0.36, 1')
        elif result >= 0 and self.item['in_dryer']:
            self.parent_layout.all_items_collection[self.item['carrier_barcode']]['status'] = 'grey'
            return eval('0.24, 0.25, 0.25, 1')
        elif result >= 0 and not self.item['in_dryer']:
            self.parent_layout.all_items_collection[self.item['carrier_barcode']]['status'] = 'blue'
            return eval('0.70, 0.04, 0.00, 1')
        elif result <= 0 and not self.item['in_dryer']:
            self.parent_layout.all_items_collection[self.item['carrier_barcode']]['status'] = 'red'
            return eval('0.16, 0.67, 0.72, 1')

    def calculate_timer_in_sec(self):
        if not self.check_datetime_format(str(self.item['start_time']), self.dt_format):
            dt = datetime.fromtimestamp(self.item['start_time'])
            self.item['start_time'] = dt.strftime(self.dt_format)
        if self.item['in_dryer']:
            time_now = datetime.strptime(str(datetime.now()), self.dt_format)
        else:
            time_now = self.item['end_time']

        start_time = datetime.strptime(str(self.item['start_time']), self.dt_format)
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(self.item['drying_start_interval']) + int(self.item['add_interval']))
        result = total_interval_sec - interval_now_sec

        return result

    @staticmethod
    def check_datetime_format(date_string, date_format):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False

