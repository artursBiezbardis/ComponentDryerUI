from services.carrier_services.setDryingIntervalService import SetDryingIntervalService
import asyncio
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class SetDryingIntervalController:

    def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):
        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:

            time.sleep(0.1)

        task = asyncio.run(SetDryingIntervalService().main(thickness_level, moisture_level, hours_greater_or_less_than_72))
        glob_var.global_async_db_queue.remove(new_queue[-1])
        return task
