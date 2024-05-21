from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class BarcodeItem(BoxLayout):
    barcode_text = StringProperty('')
    part_text = StringProperty('part name')

    def on_button_press(self):
        # Handle the button press event
        print(f'Set for {self.barcode_text}')
