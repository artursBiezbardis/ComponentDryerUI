from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from datetime import datetime


class BarcodeItem(BoxLayout):
    barcode_text = StringProperty('')
    part_text = StringProperty('part name')
    item = ObjectProperty({})

    def on_button_press(self):
        # Handle the button press event
        print(f'Set for {self.barcode_text}')

    def timer_counter(self) -> str:
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(self.item['start_time']), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(self.item['drying_start_interval']) + int(self.item['add_interval']))*3600
        result = total_interval_sec - interval_now_sec
        hours = int(result // 3600)
        minutes = int((result % 3600) // 60)

        return f"{hours} : {minutes:02d}"

