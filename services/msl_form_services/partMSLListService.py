from database import AsyncSessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class PartMSLListService:

    async def main(self, part_name):
        async with AsyncSessionLocal() as db_session:
            items_collection = {}
            task_data_repo = TaskDataRepository(db_session)
            data = await task_data_repo.get_all_part_msl_data(part_name)
            for item in data:
                items_collection[item.carrier_id] = {}
                items_collection[item.carrier_id]['thickness'] = item.thickness
                items_collection[item.carrier_id]['msl'] = item.msl
                items_collection[item.carrier_id]['hours_greater_than_72'] = item.hours_greater_than_72
                items_collection[item.carrier_id]['hours_less_then_72'] = item.hours_less_72_hours
                items_collection[item.carrier_id]['drying_start_interval'] = item.drying_start_interval

        return items_collection
