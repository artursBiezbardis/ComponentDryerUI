from database import AsyncSessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class StartDryingService:

    async def main(self, item_data_template):

        async with AsyncSessionLocal() as db_session:

            task_repo = TaskDataRepository(db_session)
            item_data_template = await task_repo.add_new_task(item_data_template)
            return item_data_template


