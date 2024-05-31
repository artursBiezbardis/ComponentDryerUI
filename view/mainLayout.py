from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import view.layouts.barcodeItem as Carrier
from view.layouts.addToDryerForm import AddToDryerForm
import controllers.carrier_controllers.addRemoveCarrierController as addCarrier
import controllers.carrier_controllers.createDryingItemController as createItem
from constants import ITEM_DATA_TEMPLATE
from controllers.drying_list_controllers.updateDryingListController import UpdateCarrierListFromDBController
from kivy.properties import ObjectProperty
from datetime import datetime


class MainLayout(GridLayout):
    popup = ObjectProperty(None)

    ADD_REMOVE_CARRIER = {'carrier_barcode': '',
                          'carrier_position': '',
                          'add_status': False,
                          'remove_status': False,
                          'status_message': ''}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drying_carrier_collection = {}
        self.add_carrier = self.ADD_REMOVE_CARRIER.copy()
        self.item_data_template = {}
        self.focus_text_input(self)
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)
        self.refresh_part_carrier_list(self)

    def update_drying_carrier_collection(self):
        self.drying_carrier_collection = UpdateCarrierListFromDBController().main()

    def part_carrier_list(self, dt):
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        self.sort_part_carrier_list_by_timer()
        if self.drying_carrier_collection:
            for item in self.drying_carrier_collection.values():
                drying_item = Carrier.BarcodeItem(
                    barcode_text=item['carrier_barcode'],
                    part_text=item['part_name'],
                    item=item,
                    location=item['carrier_position'])
                box_layout.add_widget(drying_item)

    def on_enter(self, instance):
        barcode: str = instance.text
        self.add_carrier = addCarrier.AddRemoveCarrierController(self.add_carrier,
                                                                 self.drying_carrier_collection,
                                                                 barcode).main()
        self.item_data_template = createItem.CreateDryingItemController(self.add_carrier).main()
        self.open_set_timer_form_popup()
        instance.text = ''
        self.reset_after_removing_item()
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)

        Clock.schedule_once(lambda dt: setattr(instance, 'focus', True), 1)

    def focus_text_input(self, dt):
        scanner_input = self.ids.scanner_input
        scanner_input.focus = True

    def open_set_timer_form_popup(self):
        if self.item_data_template:
            self.popup = AddToDryerForm(item_data_template=self.item_data_template)
            self.popup.main_layout = self
            self.popup.open()

    def on_dismiss_refresh_main(self):
        self.drying_carrier_collection = UpdateCarrierListFromDBController().main()
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)
        self.add_carrier = self.ADD_REMOVE_CARRIER.copy()
        self.item_data_template = ITEM_DATA_TEMPLATE.copy()
        Clock.schedule_once(self.focus_text_input, 2)

    def reset_after_removing_item(self):
        if self.add_carrier['remove_status']:
            self.add_carrier = self.ADD_REMOVE_CARRIER.copy()

    def refresh_part_carrier_list(self, dt):
        Clock.schedule_interval(self.part_carrier_list, 60)

    def sort_part_carrier_list_by_timer(self):

        item_list = self.add_timer_value_to_item()

        sorted_items_list = sorted(item_list.items(), key=lambda x: x[1]['interval_now'])

        self.drying_carrier_collection = dict(sorted_items_list)

    @staticmethod
    def timer_calculation_for_sort(item):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(item['start_time']), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item['drying_start_interval']) + int(item['add_interval'])) * 3600
        result = total_interval_sec - interval_now_sec

        return result

    def add_timer_value_to_item(self):

        new_collection = {}
        for key, item in self.drying_carrier_collection.copy().items():
            item['interval_now'] = int(self.timer_calculation_for_sort(item))
            new_collection[key] = item

        return new_collection.copy()
