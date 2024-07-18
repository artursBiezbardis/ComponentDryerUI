from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, DictProperty
from view.layouts.itemViewElement import ItemViewElement
from services.task_data_services.deleteTaskService import DeleteTaskService


class ItemViewPopup(Popup):
    main_layout = ObjectProperty(None)
    item_data = DictProperty(None)

    def __init__(self, **kwargs):
        super(ItemViewPopup, self).__init__(**kwargs)
        self.show_elements()

    def show_elements(self):
        box_layout = self.ids.scroll_box
        box_layout.clear_widgets()
        if self.item_data:

            for key, value in self.item_data.items():
                element = ItemViewElement(element_name=str(key), element_value=str(value))
                box_layout.add_widget(element)

    def remove_item(self):

        DeleteTaskService().main(self.item_data['task_id'])


