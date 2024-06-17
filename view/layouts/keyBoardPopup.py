from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from kivy.properties import ObjectProperty


class KeyBoardPopup(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)