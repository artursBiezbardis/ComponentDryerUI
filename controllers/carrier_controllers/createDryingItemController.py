from services.carrier_services.createDryingItemService import CreateDryingItemService


class CreateDryingItemController:

    def __init__(self, add_carrier):
        self.add_carrier = add_carrier

    def main(self):
        if self.add_carrier['add_status'] and not self.add_carrier['remove_status']:
            return CreateDryingItemService(self.add_carrier).main()
        return {}
