import asyncio
from services.task_data_services.deleteTaskService import DeleteTaskService
import GLOBALS as glob_var
import time
from utilities.async_queue_utilities import AsyncQueueUtilities


class DeleteTaskController:

    @staticmethod
    def main(task_id):
        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:
            time.sleep(0.1)
        asyncio.run(DeleteTaskService().main(task_id))
        glob_var.global_async_db_queue.remove(new_queue[-1])
