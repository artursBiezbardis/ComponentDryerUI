from database import SessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository
from utilities.timer_utils import TimerUtilities


class TimerUpdateService:
    def __init__(self, dryer_status: bool, add_interval_value: int):
        self.dryer_status = dryer_status
        self.add_interval_value = add_interval_value

    def main(self):
        if not self.dryer_status:
            db_session = SessionLocal()
            db_session.close()
            db_session = SessionLocal()
            task_repo = TaskDataRepository(db_session)
            drying_items = task_repo.get_all_drying_items()
            for item in drying_items:
                if not TimerUtilities().check_db_item_finished(item):
                    add_interval_value = int(item.add_interval) + self.add_interval_value
                    task_repo.update_add_time(item.carrier_id, add_interval_value)

            db_session.close()


