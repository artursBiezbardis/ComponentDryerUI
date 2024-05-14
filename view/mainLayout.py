from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import view.layouts.barcodeItem as Packaging
import controllers.addCarrierController as addCarrier
import controllers.startCarrierItemController as startCarrier


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.barcodes_collection = []
        self.drying_carrier_collection = {}
        self.add_carrier = {'carrier_barcode': '', 'carrier_position': '', 'status_message': ''}
        self.part_packaging_list()
        self.focus_text_input()

    def part_packaging_list(self):
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        for barcode in self.barcodes_collection:
            barcode_item = Packaging.BarcodeItem(barcode_text=barcode, part_text='part name')
            box_layout.add_widget(barcode_item)

    def on_enter(self, instance):
        # Process the barcode entered in TextInput
        barcode: str = instance.text
        if barcode not in self.drying_carrier_collection:
            self.add_carrier = addCarrier.AddCarrierController(self.add_carrier, barcode).main()
        else:
            self.add_carrier['status_message'] = 'Carrier '+self.add_carrier['carrier_barcode']+' is in Dryer!!'
        print(f"Barcode submitted: {barcode}")
        # Update some status, e.g., a label or another part of your UI

        self.barcodes_collection.append(barcode)
        # Clear the input for next scan
        instance.text = ''
        # Optionally, reset focus after a delay
        self.part_packaging_list()
        Clock.schedule_once(lambda dt: setattr(instance, 'focus', True), 1)

    def focus_text_input(self):
        scanner_input = self.ids.scanner_input
        scanner_input.focus = True
