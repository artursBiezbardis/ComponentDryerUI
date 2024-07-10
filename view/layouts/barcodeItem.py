from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from datetime import datetime
from utilities.timer_utils import TimerUtilities


class BarcodeItem(BoxLayout):
    barcode_text = StringProperty('')
    part_text = StringProperty('part name')
    location = StringProperty('')
    item = ObjectProperty({})

    def on_button_press(self):
        # Handle the button press event
        print(f'Set for {self.barcode_text}')

    def timer_counter(self) -> str:
        result = self.calculate_timer_in_sec()
        hours = int(result // 3600)
        minutes = int((result % 3600) // 60)
        if result <= 0:
            return '00 : 00'
        return f"{hours} : {minutes:02d}"

    def set_list_item_color(self):
        result = TimerUtilities().time_left(self.item)
        if result <= 0:

            return eval('0.34, 0.59, 0.36, 1')

        return eval('0.24, 0.25, 0.25, 1')

    def calculate_timer_in_sec(self):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(self.item['start_time']), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(self.item['drying_start_interval']) + int(self.item['add_interval']))
        result = total_interval_sec - interval_now_sec

        return result


