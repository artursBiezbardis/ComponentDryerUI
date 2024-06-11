from database import SessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class StartDryingService:

    def main(self, item_data_template):

        return self.add_task_to_db(item_data_template)

    def add_task_to_db(self, item_data_template):
        db_session = SessionLocal()
        db_session.close()

        db_session = SessionLocal()
        task_repo = TaskDataRepository(db_session)
        item_data_template = task_repo.add_new_task(item_data_template)
        db_session.close()
        return item_data_template
