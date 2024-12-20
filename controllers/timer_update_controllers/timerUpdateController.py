from services.timer_update_services.timerUpdateService import TimerUpdateService
import asyncio
import GLOBALS as glob_var
from utilities.async_queue_utilities import AsyncQueueUtilities


class TimerUpdateController:

    def __init__(self, dryer_status: bool, add_interval_value: int, after_dryer_update=False):
        self.dryer_status = dryer_status
        self.add_interval_value = add_interval_value
        self.after_dryer_update = after_dryer_update

    def main(self):

        new_queue = AsyncQueueUtilities().add_item_to_queue(glob_var.global_async_db_queue)

        while glob_var.global_async_db_queue[0] != new_queue[-1]:
            pass

        asyncio.run(TimerUpdateService(self.dryer_status, self.add_interval_value, self.after_dryer_update).main())
        glob_var.global_async_db_queue.remove(new_queue[-1])
