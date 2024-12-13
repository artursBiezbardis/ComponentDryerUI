from kivy.uix.popup import Popup
from kivy.properties import DictProperty, ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.clock import Clock
import config


class InfoPopup(Popup):
    item_data_template = DictProperty({})
    info = StringProperty(None)
    main_layout = ObjectProperty(None)
    alert_message = BooleanProperty(False)
    time = NumericProperty(2)
    dismiss_button = BooleanProperty(False)
    ok_button = BooleanProperty(False)
    enable_alarm_schedule = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.main_layout:
            self.main_layout.ids.scanner_input.readonly = True
        if not self.dismiss_button and not self.ok_button:
            self.hide_button(self.ids.dismiss_button)
            self.hide_button(self.ids.ok_button)
            Clock.schedule_once(self.dismiss_time, self.time)
        else:
            if not self.dismiss_button:
                self.hide_button(self.ids.dismiss_button)
            if not self.ok_button:
                self.hide_button(self.ids.ok_button)
        self.connection_timeout = config.CONNECTION_TIMEOUT['connection_timeout_for_alert_message']

    def dismiss_time(self, dt):
        self.dismiss()
        if self.main_layout:
            self.main_layout.ids.scanner_input.readonly = False

    def info_window_color(self):
        if self.alert_message:

            return eval('0.96, 0.29, 0.25, 1')

        return eval('0.34, 0.59, 0.36, 1')

    def hide_button(self, instance):
        instance.opacity = 1
        instance.disabled = True

    def show_button(self, instance):
        instance.opacity = 1
        instance.disabled = False

    def on_press_ok(self):
        self.main_layout.info_popup_ok_button_attribute_1 = True
        self.main_layout.info_popup_ok_button_attribute_2 = True
        self.main_layout.add_remove_carrier['message_dismiss_button'] =False
        self.main_layout.add_remove_carrier['message_ok_button'] =False
        if self.enable_alarm_schedule:
            self.main_layout.alarm = Clock.schedule_interval(self.main_layout.dryer_alarms, self.connection_timeout)

    def on_press_dismiss(self):
        self.main_layout.info_popup_dismiss_button_attribute_1 = True
        self.main_layout.info_popup_dismiss_button_attribute_2 = True
        self.main_layout.add_remove_carrier['message_dismiss_button'] = False
        self.main_layout.add_remove_carrier['message_ok_button'] = False
        if self.enable_alarm_schedule:
            self.main_layout.alarm = Clock.schedule_interval(self.main_layout.dryer_alarms, self.connection_timeout)

    def close_main_layout_popups(self):
        for popup in self.main_layout.popups:
            popup.dismiss()

    def on_enter_recycle(self):

        self.main_layout.on_enter()

