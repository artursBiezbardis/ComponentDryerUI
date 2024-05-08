from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.barcodes_collection = []
        self.part_packaging_list()
        self.focus_text_input()


    def part_packaging_list(self):
        # Access the BoxLayout inside ScrollView by ID
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        # Dynamically add 10 more buttons
        for barcode in self.barcodes_collection:
            barcode_label = Label(text=f'{barcode}', size_hint_y=None, height=50)
            box_layout.add_widget(barcode_label)
            part_label = Label(text=f'part name', size_hint_y=None, height=50)
            box_layout.add_widget(part_label)
            btn = Button(text=f'Set', size_hint_y=None, height=50)
            box_layout.add_widget(btn)

    def on_enter(self, instance):
        # Process the barcode entered in TextInput
        barcode = instance.text
        print(f"Barcode submitted: {barcode}")
        # Update some status, e.g., a label or another part of your UI
        self.barcodes_collection.append(barcode)
        # Clear the input for next scan
        instance.text = ''
        # Optionally, reset focus after a delay
        self.part_packaging_list()
        Clock.schedule_once(lambda dt: setattr(instance, 'focus', True), 3)

    # def scanner_input(self):
    #     scanner_input = self.ids.scanner_input
    #     scanner_input.focus = True
    #     self.barcodes_collection.add(scanner_input.text)
    #     scanner_input.text = ''
    #     Clock.schedule_once(self.focus_text_input, 3)
    #

    def focus_text_input(self):
        scanner_input = self.ids.scanner_input
        scanner_input.focus = True
