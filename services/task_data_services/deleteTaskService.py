from database import SessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class DeleteTaskService:

    def main(self, task_id):
        db_session = SessionLocal()
        db_session.close()

        db_session = SessionLocal()
        task_repo = TaskDataRepository(db_session)
        task_repo.delete_task_by_id(task_id)
        db_session.close()
