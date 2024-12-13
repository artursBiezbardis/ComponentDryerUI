from services.timer_update_services.deviceOffIntervalService import DeviceOffIntervalService
from utilities.async_queue_utilities import AsyncQueueUtilities
import asyncio
import time
import GLOBALS as glob_var

class DeviceOffIntervalController:

    def main(self):

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:

            time.sleep(0.02)

        task = asyncio.run(DeviceOffIntervalService().main())
        glob_var.global_async_db_queue.remove(new_queue[-1])
        return task

