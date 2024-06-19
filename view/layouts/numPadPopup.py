from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class NumPadPopup(Popup):

    layout_for_num_pad = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.input_text.focus = True

    def type_letter(self, letter):
        self.ids.input_text.text = self.ids.input_text.text + letter

    def delete_one_letter(self):
        self.ids.input_text.text = self.ids.input_text.text[:-1]

    def enter_text(self):
        self.layout_for_num_pad.enter_num_pad_text(self.ids.input_text)
        self.layout_for_num_pad.enable_submit()
        self.dismiss()


