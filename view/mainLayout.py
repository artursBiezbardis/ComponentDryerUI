from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import view.layouts.barcodeItem as Carrier
from view.layouts.addToDryerForm import AddToDryerForm
import controllers.addRemoveCarrierController as addCarrier
import controllers.createDryingItemController as createItem


class MainLayout(GridLayout):

    _add_remove_carrier = {'carrier_barcode': '',
                           'carrier_position': '',
                           'add_status': False,
                           'remove_status': False,
                           'status_message': ''}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.barcodes_collection = []
        self.drying_carrier_collection = {}
        self.add_carrier = self._add_remove_carrier
        self.item_data_template = {}
        self.part_carrier_list()
        self.focus_text_input()

    def part_carrier_list(self):
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        for item in self.drying_carrier_collection.values():
            drying_item = Carrier.BarcodeItem(barcode_text=item['carrier_barcode'], part_text=item['part_name'])
            box_layout.add_widget(drying_item)

    def on_enter(self, instance):
        # Process the barcode entered in TextInput
        barcode: str = instance.text
        self.add_carrier = addCarrier.AddRemoveCarrierController(self.add_carrier,
                                                                 self.drying_carrier_collection,
                                                                 barcode).main()
        self.item_data_template = createItem.CreateDryingItemController(self.add_carrier).main()

        if self.item_data_template:
            self.drying_carrier_collection[self.item_data_template['carrier_barcode']] = self.item_data_template
            self.add_carrier = self._add_remove_carrier
            self.open_set_timer_form_popup()

        # 1. add reset add carrier
        # self.barcodes_collection.append(barcode)
        # Clear the input for next scan
        instance.text = ''
        # Optionally, reset focus after a delay

        self.part_carrier_list()
        Clock.schedule_once(lambda dt: setattr(instance, 'focus', True), 1)

    def focus_text_input(self):
        scanner_input = self.ids.scanner_input
        scanner_input.focus = True

    def open_set_timer_form_popup(self):
        popup = AddToDryerForm(item_data_template=self.item_data_template)
        popup.open()
