from database import AsyncSessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class DeleteTaskService:

    async def main(self, task_id):
        async with AsyncSessionLocal() as db_session:

            task_repo = TaskDataRepository(db_session)
            await task_repo.delete_task_by_id(task_id)
