from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import config
import view.layouts.barcodeItem as Carrier
from view.layouts.addToDryerForm import AddToDryerForm
from view.layouts.addValuePopup import AddValuePopup
from view.layouts.infoPopup import InfoPopup
from view.layouts.keyboardPopup import KeyboardPopup
from view.layouts.allItemsList import AllItemsList
import controllers.carrier_controllers.addRemoveCarrierController as addCarrier
import controllers.carrier_controllers.createDryingItemController as createItem
from constants import ITEM_DATA_TEMPLATE
from controllers.drying_list_controllers.updateDryingListController import UpdateCarrierListFromDBController
from kivy.properties import ObjectProperty
from controllers.dryer_communications_controllers.xtremeDryerCommunicationsController import XtremeDryerCommunicationsController
from controllers.last_app_activity_controller.lastAppActivityRegisterController import LastAppActivityRegisterController
from utilities.timer_utils import TimerUtilities
from utilities.format_string_utilities import FormatStringUtilities
from config import TIMER_SETTINGS
from controllers.timer_update_controllers.deviceOffIntervalController import DeviceOffIntervalController
from controllers.timer_update_controllers.timerUpdateController import TimerUpdateController
from controllers.dryer_alarm_controllers.dryerAlarmController import DryerAlarmController


class MainLayout(GridLayout):
    popup = ObjectProperty(None)
    add_part_name_popup = ObjectProperty(None)
    info_popup = ObjectProperty(None)

    ADD_REMOVE_CARRIER = {'carrier_barcode': '',
                          'carrier_position': '',
                          'add_status': False,
                          'remove_status': False,
                          'status_message': '',
                          'alert_message': False,
                          'message_dismiss_button': False,
                          'message_ok_button': False,
                          'on_enter_recycle': False
                          }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.info_popup_ok_button_attribute_1 = False
        self.info_popup_dismiss_button_attribute_1 = False
        self.app_start_event = None
        self.last_action_interval = DeviceOffIntervalController().main()
        self.drying_carrier_collection = {}
        self.add_remove_carrier = self.ADD_REMOVE_CARRIER.copy()
        self.item_data_template = ITEM_DATA_TEMPLATE.copy()
        self.focus_text_input(self)
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)
        self.refresh_part_carrier_list(self)
        self.popups = []
        self.dryer_status_output = {'dryer_status': False, 'dryer_status_info': 'no connection'}
        self.dryer_status = self.dryer_status_output['dryer_status']
        self.set_dryer_status_info(self.dryer_status_output['dryer_status_info'])
        self.set_status_color(self.dryer_status)
        self.last_action_info = 'app start'
        self.set_last_action_info()

    def update_drying_carrier_collection(self):
        self.drying_carrier_collection = UpdateCarrierListFromDBController().main()

    def part_carrier_list(self, dt):
        self.update_drying_carrier_collection()
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        if self.drying_carrier_collection:
            self.sort_part_carrier_list_by_timer()
            for item in self.drying_carrier_collection.values():
                drying_item = Carrier.BarcodeItem(
                    barcode_text=item['carrier_barcode'],
                    part_text=item['part_name'],
                    item=item,
                    location=item['carrier_position'])
                box_layout.add_widget(drying_item)

    def on_enter(self, instance):

        barcode: str = instance.text
        instance.text = ''
        self.add_remove_carrier = addCarrier.AddRemoveCarrierController(self.add_remove_carrier,
                                                                 self.drying_carrier_collection,
                                                                 barcode).main()
        self.item_data_template = createItem.CreateDryingItemController(self.add_remove_carrier, self.item_data_template).main()
        self.last_action_info = self.add_remove_carrier['status_message']
        self.set_last_action_info()
        self.set_custom_part_popup()
        self.open_set_timer_form_popup()
        self.show_info_popup(self.add_remove_carrier)
        self.reset_after_removing_item()
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)
        self.disable_on_enter_focus(instance)

    def focus_text_input(self, dt):
        scanner_input = self.ids.scanner_input
        scanner_input.focus = True

    def open_set_timer_form_popup(self):
        if self.item_data_template['part_name'] and not self.item_data_template['popup_opened']:
            self.popup = AddToDryerForm(item_data_template=self.item_data_template, main_layout=self, auto_dismiss=False)
            self.popups.append(self.popup)
            self.popup.main_layout = self
            self.item_data_template['popup_opened'] = True
            self.popup.open()

    def on_dismiss_refresh_main(self):
        self.drying_carrier_collection = UpdateCarrierListFromDBController().main()
        self.update_drying_carrier_collection()
        self.part_carrier_list(self)
        self.add_remove_carrier = self.ADD_REMOVE_CARRIER.copy()
        self.item_data_template = ITEM_DATA_TEMPLATE.copy()
        self.ids.scanner_input.readonly = False
        self.add_remove_carrier['message_dismiss_button']: False
        self.add_remove_carrier['message_ok_button']: False
        Clock.schedule_once(self.focus_text_input, 1)

    def on_ok_refresh_main(self):
        if not self.add_remove_carrier['on_enter_recycle']:
            self.ids.scanner_input.readonly = False
            self.add_remove_carrier['message_dismiss_button']: False
            self.add_remove_carrier['message_ok_button']: False
            Clock.schedule_once(self.focus_text_input, 1)
        else:
            self.add_remove_carrier['message_dismiss_button']: False
            self.add_remove_carrier['message_ok_button']: False
            self.ids.scanner_input.text = self.add_remove_carrier['carrier_barcode']
            self.add_remove_carrier['on_enter_recycle'] = True
            self.on_enter(self.ids.scanner_input)
            Clock.schedule_once(self.focus_text_input, 1)

    def reset_after_removing_item(self):
        if self.add_remove_carrier['remove_status']:
            self.add_remove_carrier = self.ADD_REMOVE_CARRIER.copy()

    def sort_part_carrier_list_by_timer(self):

        item_list = self.add_timer_value_to_item()
        sorted_items_list = sorted(item_list.items(), key=lambda x: x[1]['interval_now'])
        self.drying_carrier_collection = dict(sorted_items_list)

    def add_timer_value_to_item(self):

        new_collection = {}
        for key, item in self.drying_carrier_collection.copy().items():
            item['interval_now'] = int(TimerUtilities().time_left(item))
            new_collection[key] = item

        return new_collection.copy()

    def set_custom_part_popup(self):
        if not self.item_data_template['part_name'] and self.add_remove_carrier['add_status']:
            self.add_part_name_popup = AddValuePopup(value_name='Part Name',
                                                     item_data_template=self.item_data_template,
                                                     auto_dismiss=False,
                                                     layout_for_popup=self,
                                                     enable_alarm_schedule=True
                                                     )
            self.popups.append(self.add_part_name_popup)
            self.add_part_name_popup.layout_for_popup = self
            self.add_part_name_popup.open()

    def show_info_popup(self, add_remove_carrier):
        if add_remove_carrier['status_message']:
            self.alarm.cancel()
            self.info_popup = InfoPopup(info=add_remove_carrier['status_message'],
                                        main_layout=self,
                                        alert_message=add_remove_carrier['alert_message'],
                                        auto_dismiss=False,
                                        ok_button=add_remove_carrier['message_dismiss_button'],
                                        dismiss_button=add_remove_carrier['message_ok_button'],
                                        enable_alarm_schedule=True
                                        )
            self.popups.append(self.info_popup)
            self.info_popup.open()

    def check_and_update_dryer_status(self, dt):

        LastAppActivityRegisterController().main()
        self.dryer_status_output = XtremeDryerCommunicationsController().main()
        self.dryer_status: bool = self.dryer_status_output['dryer_status']
        TimerUpdateController(self.dryer_status, TIMER_SETTINGS['dryer_status_request']).main()
        self.set_status_color(self.dryer_status)
        self.set_dryer_status_info(self.dryer_status_output['dryer_status_info'])

    def set_status_color(self, dryer_status):
        if dryer_status:
            self.ids.status.color = config.COLORS['green_status']
        else:
            self.ids.status.color = config.COLORS['red_status']

    def set_dryer_status_info(self, dryer_status_info):
        self.ids.status_text.text = 'Status info:   \n\n'+dryer_status_info
        if self.dryer_status:
            self.ids.status_text.color = config.COLORS['green_status']
        else:
            self.ids.status_text.color = config.COLORS['red_status']

    def set_last_action_info(self):
        self.ids.last_action_text.text = 'Last action:   \n\n'+FormatStringUtilities().break_string_in_lines(
            self.last_action_info, 14)
        self.ids.last_action_text.color = [0.11, 0.32, 0.49, 1]

    def refresh_part_carrier_list(self, dt):
        Clock.schedule_once(self.popup_for_timer_after_devices_off, 1)
        self.app_start_event = Clock.schedule_interval(self.on_app_start_set_timer, 2)
        Clock.schedule_interval(self.check_and_update_dryer_status, TIMER_SETTINGS['dryer_status_request'])
        Clock.schedule_interval(self.part_carrier_list, TIMER_SETTINGS['refresh_drying_list'])

    def disable_on_enter_focus(self, instance):
        self.ids.scanner_input.focus = False
        if not self.item_data_template['popup_opened']:
            Clock.schedule_once(lambda dt: setattr(instance, 'focus', True), 1)

    def open_key_board(self):
        key_board = KeyboardPopup(layout_for_keyboard=self)
        key_board.open()

    def enter_keyboard_text(self, keyboard_text_instance):
        self.on_enter(keyboard_text_instance)

    def popup_for_timer_after_devices_off(self, dt):

        if not self.info_popup_ok_button_attribute_1:
            popup = InfoPopup(
                auto_dismiss=False,
                dismiss_button=True,
                ok_button=True,
                info='Update timers for carrier\'s,\n after UI device was off?',
                main_layout=self,
                alert_message=True,
                enable_alarm_schedule=True
            )
            self.popups.append(popup)
            popup.open()

    def on_app_start_set_timer(self, dt):
        if self.info_popup_ok_button_attribute_1:
            TimerUpdateController(False, int(self.last_action_interval)).main()
            self.on_dismiss_refresh_main()
            self.info_popup_ok_button_attribute_1 = False
            self.app_start_event.cancel()

    def open_all_item_list(self):
        popup = AllItemsList(main_layout=self)
        popup.open()

    def dryer_alarms(self, dt):
        message = DryerAlarmController().main()
        if message['alert']:
            self.alarm.cancel()
            popup = InfoPopup(
                auto_dismiss=False,
                dismiss_button=True,
                info=message['alert_message'],
                main_layout=self,
                alert_message=True,
                enable_alarm_schedule=True
            )
            self.popups.append(popup)
            popup.open()
