from services.drying_list_services.updateCarrierListFromDBService import UpdateCarrierListFromDBService
import asyncio
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class UpdateCarrierListFromDBController:

    def main(self):

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:

            time.sleep(0.1)
        task = asyncio.run(UpdateCarrierListFromDBService().main())
        glob_var.global_async_db_queue.remove(new_queue[-1])
        return task
