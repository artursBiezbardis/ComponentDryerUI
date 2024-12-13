import asyncio
from services.timer_update_services.lastAppActivityRegisterService import LastAppActivityRegisterService
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class LastAppActivityRegisterController:

    @staticmethod
    def main():

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:

            time.sleep(0.1)

        asyncio.run(LastAppActivityRegisterService().main())
        glob_var.global_async_db_queue.remove(new_queue[-1])

