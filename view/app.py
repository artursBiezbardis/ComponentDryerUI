from kivy.app import App
from kivy.lang import Builder
from view.mainLayout import MainLayout
from kivy.core.window import Window


class DryerApp(App):
    def build(self):
        Window.size = (640, 480)
        Builder.load_file('kv_files/main.kv')
        return MainLayout()