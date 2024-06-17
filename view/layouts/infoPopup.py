from kivy.uix.popup import Popup
from kivy.properties import DictProperty, ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.clock import Clock


class InfoPopup(Popup):
    item_data_template = DictProperty({})
    info = StringProperty(None)
    main_layout = ObjectProperty(None)
    alert_message = BooleanProperty(False)
    time = NumericProperty(2)
    dismiss_button = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout.ids.scanner_input.readonly = True
        if not self.dismiss_button:
            Clock.schedule_once(self.dismiss_time, self.time)

    def dismiss_time(self, dt):
        self.dismiss()
        self.main_layout.ids.scanner_input.readonly = False

    def info_window_color(self):
        if self.alert_message:

            return eval('0.96, 0.29, 0.25, 1')

        return eval('0.34, 0.59, 0.36, 1')
