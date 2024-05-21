
from services.addCarrierService import AddCarrierService
from services.removeCarierService import RemoveCarrierService


class AddRemoveCarrierController:

    def __init__(self, add_remove_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.add_remove_carrier = add_remove_carrier
        self.barcode = barcode
        self.drying_carrier_collection = drying_carrier_collection

    def main(self) -> dict:
        add_carrier = AddCarrierService(self.add_remove_carrier, self.drying_carrier_collection, self.barcode)
        remove_carrier = RemoveCarrierService(self.add_remove_carrier, self.drying_carrier_collection, self.barcode)

        if self.barcode not in self.drying_carrier_collection:
            self.add_remove_carrier = add_carrier.main()
        elif self.barcode in self.drying_carrier_collection:
            self.add_remove_carrier = remove_carrier.main()

        return self.add_remove_carrier

