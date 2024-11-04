from services.carrier_services.startDryingService import StartDryingService
import asyncio
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class StartDryingController:

    def main(self, item_data_template):

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)
        while glob_var.global_async_db_queue[0] != new_queue[-1]:
            time.sleep(0.1)
        asyncio.run(StartDryingService().main(item_data_template))
        glob_var.global_async_db_queue.remove(new_queue[-1])
