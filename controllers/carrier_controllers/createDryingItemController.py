from services.carrier_services.createDryingItemService import CreateDryingItemService


class CreateDryingItemController:

    def __init__(self, add_carrier, item_data_template):
        self.add_carrier = add_carrier
        self.item_data_template = item_data_template.copy()

    def main(self):
        if self.add_carrier['add_status'] and not self.add_carrier['remove_status']:
            return CreateDryingItemService(self.add_carrier).main()
        return self.item_data_template
