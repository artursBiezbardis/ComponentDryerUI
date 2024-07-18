from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty, ObjectProperty


class AllListItem(BoxLayout):
    item = DictProperty({})
    add_to_dryer_form = ObjectProperty(None)
    parent_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dt_format = "%Y-%m-%d %H:%M:%S.%f"

    def set_list_item_color(self):
        if self.item['status'] == 'green':
            return eval('0.34, 0.59, 0.36, 0.3')

        elif self.item['status'] == 'grey':
            return eval('0.24, 0.25, 0.25, 0.3')

        elif self.item['status'] == 'red':
            return eval('0.70, 0.04, 0.00, 0.3')

        elif self.item['status'] == 'blue':
            return eval('0.16, 0.67, 0.72, 0.3')

    def set_data_spinner(self):

        return str(self.item[self.parent_layout.ids.data_spinner.text])

    def open_view(self):
        self.parent_layout.open_data_view(self.item)



