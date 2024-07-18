from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from services.all_items_list_service.allItemsListService import AllItemsListService
from view.layouts.allListItem import AllListItem
from datetime import datetime
from view.layouts.keyboardPopup import KeyboardPopup
from view.layouts.itemViewPopup import ItemViewPopup


class AllItemsList(Popup):
    main_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AllItemsList, self).__init__(**kwargs)
        self.find = ''
        self._sort_revers = False
        self.sort_by = 'task_id'
        self.all_items_collection = self.get_items_collection()
        self.part_carrier_list()
        self.ids.find.bind(text=self.find_items)

    def part_carrier_list(self):
        box_layout = self.ids.scroll_box
        self.sort_list()
        box_layout.clear_widgets()
        if self.all_items_collection:
            for item in self.all_items_collection.values():
                item = AllListItem(item=item, parent_layout=self)
                box_layout.add_widget(item)

    def get_items_collection(self):

        return AllItemsListService().main()

    def refresh_main_layout(self):

        self.main_layout.on_dismiss_refresh_main()

    def sort_list(self):
        if self.sort_by == 'start_time' or self.sort_by == 'end_time':
            processed_items_collection = {key: self.preprocess_time(
                value) for key, value in self.all_items_collection.items()}
            self.all_items_collection = dict(
                sorted(processed_items_collection.items(),
                       key=lambda item: item[1][self.sort_by],
                       reverse=self._sort_revers))
        else:
            self.all_items_collection = dict(
                sorted(self.all_items_collection.items(),
                       key=lambda item: item[1][self.sort_by],
                       reverse=self._sort_revers))

    def preprocess_time(self, date_time):
        value = date_time
        if not isinstance(value[self.sort_by], float):
            if value[self.sort_by]:
                dt = datetime(value[self.sort_by].year,
                              value[self.sort_by].month,
                              value[self.sort_by].day,
                              value[self.sort_by].hour,
                              value[self.sort_by].minute,
                              value[self.sort_by].second,
                              value[self.sort_by].microsecond)
            else:
                dt = datetime(1988, 1, 1, 0, 0, 0, 0)
            value[self.sort_by] = dt.timestamp()

        return value

    def sort_revers(self):
        if self._sort_revers:
            self._sort_revers = False
            self.ids.revers_sort.text = '\u25B2'
        else:
            self._sort_revers = True
            self.ids.revers_sort.text = '\u25BC'

    def find_items(self, instance, text):
        if len(self.find) > len(text):
            self.all_items_collection = self.get_items_collection()
        items_found = {}
        collection = self.all_items_collection
        for key, item in collection.items():
            for name, value in item.items():
                if value:
                    if str(text).lower() in str(value).lower():
                        items_found[key] = item
                        break
        self.all_items_collection = items_found
        self.part_carrier_list()
        self.find = text

    def find_items_on_remove(self):
        text = self.ids.find.text
        items_found = {}
        collection = self.all_items_collection
        for key, item in collection.items():
            for name, value in item.items():
                if value:
                    if str(text).lower() in str(value).lower():
                        items_found[key] = item
                        break
        self.all_items_collection = items_found
        self.part_carrier_list()
        self.find = text

    def open_key_board(self):
        key_board = KeyboardPopup(layout_for_keyboard=self)
        key_board.open()

    def enter_keyboard_text(self, keyboard_text_instance):
        self.ids.find.text = keyboard_text_instance.text

    def open_data_view(self, item_data):

        popup = ItemViewPopup(main_layout=self, item_data=item_data)
        popup.open()

    def refresh_layout(self):
        self.all_items_collection = self.get_items_collection()
        self.part_carrier_list()
