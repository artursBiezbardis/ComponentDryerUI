from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ItemViewElement(BoxLayout):

    element_name = StringProperty('')
    element_value = StringProperty('')

    def __init__(self, **kwargs):
        super(ItemViewElement, self).__init__(**kwargs)

