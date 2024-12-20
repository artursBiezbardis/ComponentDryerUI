from services.carrier_services.createDryingItemService import CreateDryingItemService
import asyncio
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class CreateDryingItemController:

    def __init__(self, add_carrier, item_data_template):
        self.add_carrier = add_carrier
        self.item_data_template = item_data_template.copy()

    def main(self):
        if self.add_carrier['add_status'] and not self.add_carrier['remove_status']:

            new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)
            while glob_var.global_async_db_queue[0] != new_queue[-1]:
                time.sleep(0.1)
            task = asyncio.run(CreateDryingItemService(self.add_carrier).main())
            glob_var.global_async_db_queue.remove(new_queue[-1])

            return task

        return self.item_data_template
