from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from view.layouts.keyboardPopup import KeyboardPopup
from kivy.clock import Clock
import config
import re


class AddValuePopup(Popup):
    item_data_template = DictProperty({})
    layout_for_popup = ObjectProperty(None)
    value_name = StringProperty(None)
    user_input = StringProperty('')
    enable_alarm_schedule = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout_for_popup.ids.scanner_input.focus = False
        self.layout_for_popup.ids.scanner_input.readonly = True
        self.ids.text_input.focus = True
        self.connection_timeout = config.CONNECTION_TIMEOUT['connection_timeout_for_alert_message']
        # self.layout_for_popup.alarm.diasabled()

    def refresh_main_layout(self):
        self.layout_for_popup.on_dismiss_refresh_main()

    def on_text_change(self):
        if not bool(re.match(r"^\s*$", self.ids.text_input.text)):
            self.ids.ok.disabled = False
        if bool(re.match(r"^\s*$", self.ids.text_input.text)):
            self.ids.ok.disabled = True

    def submit_value(self):
        self.layout_for_popup.item_data_template['part_name'] = self.ids.text_input.text
        self.layout_for_popup.ids.scanner_input.readonly = False
        self.layout_for_popup.open_set_timer_form_popup()
        self.layout_for_popup.alarm = Clock.schedule_interval(self.layout_for_popup.dryer_alarms, self.connection_timeout)

    def open_key_board(self):
        key_board = KeyboardPopup(layout_for_keyboard=self)
        key_board.open()

    def enter_keyboard_text(self, keyboard_text_instance):
        self.ids.text_input.text = keyboard_text_instance.text
