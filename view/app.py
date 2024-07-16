# from kivy.config import Config
# Config.set('graphics', 'fullscreen', 'True')

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from view.mainLayout import MainLayout


class DryerApp(App):
    def build(self):
        Window.maximize()
        Builder.load_file('kv_files/main.kv')
        Builder.load_file('kv_files/barcode_item.kv')
        Builder.load_file('kv_files/add_to_dryer_form.kv')
        Builder.load_file('kv_files/add_value_popup.kv')
        Builder.load_file('kv_files/info_popup.kv')
        Builder.load_file('kv_files/keyboard_popup.kv')
        Builder.load_file('kv_files/num_pad_popup.kv')
        Builder.load_file('kv_files/part_msl_item.kv')
        Builder.load_file('kv_files/all_items_list.kv')
        Builder.load_file('kv_files/all_list_item.kv')
        Window.clearcolor = (0.12, 0.12, 0.13, 1)
        return MainLayout()
