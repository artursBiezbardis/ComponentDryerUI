from services.carrier_services.addCarrierService import AddCarrierService
from services.carrier_services.removeCarierService import RemoveCarrierService
import asyncio
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class AddRemoveCarrierController:

    def __init__(self, add_remove_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.add_remove_carrier = add_remove_carrier.copy()
        self.barcode = barcode.lower()
        self.drying_carrier_collection = drying_carrier_collection

    def main(self) -> dict:

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:
            time.sleep(0.1)

        if self.barcode not in self.drying_carrier_collection:
            add_carrier = AddCarrierService(self.add_remove_carrier, self.drying_carrier_collection, self.barcode)
            self.add_remove_carrier = asyncio.run(add_carrier.main())
        elif self.barcode in self.drying_carrier_collection:
            remove_carrier = RemoveCarrierService(self.add_remove_carrier, self.drying_carrier_collection, self.barcode)
            self.add_remove_carrier = asyncio.run(remove_carrier.main())

        glob_var.global_async_db_queue.remove(new_queue[-1])
        return self.add_remove_carrier

