from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from view.layouts.keyboardPopup import KeyboardPopup

class AddValuePopup(Popup):
    item_data_template = DictProperty({})
    layout_for_popup = ObjectProperty(None)
    value_name = StringProperty(None)
    user_input = StringProperty('')

    def __init__(self, **kwargs):
        super(AddValuePopup, self).__init__(**kwargs)

    def refresh_main_layout(self):
        self.layout_for_popup.on_dismiss_refresh_main()

    def on_text_change(self):
        self.ids.ok.disabled = False

    def submit_value(self):
        self.layout_for_popup.item_data_template['part_name'] = self.ids.text_input.text
        self.layout_for_popup.ids.scanner_input.readonly = False
        self.layout_for_popup.open_set_timer_form_popup()


    def open_key_board(self):
        key_board = KeyboardPopup(layout_for_keyboard=self)
        key_board.open()

    def enter_keyboard_text(self, keyboard_text_instance):
        self.ids.text_input.text = keyboard_text_instance.text
