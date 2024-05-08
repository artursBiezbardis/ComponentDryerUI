from kivy.app import App
from kivy.lang import Builder
from view.mainLayout import MainLayout


class DryerApp(App):
    def build(self):
        Builder.load_file('kv_files/main.kv')
        return MainLayout()