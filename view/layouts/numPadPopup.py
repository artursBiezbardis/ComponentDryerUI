from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class NumPadPopup(Popup):

    layout_for_keyboard = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def type_letter(self, letter):
        self.ids.input_text.text = self.ids.input_text.text + letter

    def delete_one_letter(self):
        self.ids.input_text.text = self.ids.input_text.text[:-1]

    def enter_text(self):
        self.layout_for_keyboard.enter_keyboard_text(self.ids.input_text)
        self.dismiss()
