from kivy.uix.popup import Popup
from kivy.properties import DictProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class AddValuePopup(Popup):
    item_data_template = DictProperty({})
    main_layout = ObjectProperty(None)
    value_name = StringProperty(None)
    user_input = StringProperty('')

    def __int__(self, **kwargs):
        super(AddValuePopup, self).__init__(**kwargs)
        self.main_layout.ids.scanner_input.readonly = True

    def refresh_main_layout(self):
        self.main_layout.on_dismiss_refresh_main()

    def on_text_change(self, instance, value):
        self.ids.ok.disabled = False

    def submit_value(self):
        self.main_layout.item_data_template['part_name'] = self.ids.text_input.text
        self.main_layout.ids.scanner_input.readonly = False
