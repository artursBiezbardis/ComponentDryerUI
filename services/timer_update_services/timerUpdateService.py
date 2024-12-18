from database import AsyncSessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository
from utilities.timer_utils import TimerUtilities


class TimerUpdateService:
    def __init__(self, dryer_status: bool, add_interval_value: int, after_dryer_update=False):
        self.dryer_status = dryer_status
        self.add_interval_value = add_interval_value
        self.after_dryer_update = after_dryer_update

    async def main(self):
        if not self.dryer_status:
            async with AsyncSessionLocal() as db_session:
                task_repo = TaskDataRepository(db_session)
                drying_items = await task_repo.get_all_drying_items()

                for item in drying_items:
                    if not TimerUtilities().check_db_item_finished(item):
                        add_interval_value = int(item.add_interval) + self.add_interval_value
                        await task_repo.update_add_time(item.id, add_interval_value)
                    if self.after_dryer_update:
                        if TimerUtilities().check_db_item_finished(item):
                            add_interval_value = int(item.add_interval) + self.add_interval_value
                            await task_repo.reset_finished_task(item.id)
                            await task_repo.update_add_time(item.id, add_interval_value)
