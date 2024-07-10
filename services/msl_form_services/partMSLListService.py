from database import SessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class PartMSLListService:

    def main(self, part_name):
        db_session = SessionLocal()
        db_session.close()
        db_session = SessionLocal()
        items_collection = {}
        task_data_repo = TaskDataRepository(db_session)
        data = task_data_repo.get_all_part_msl_data(part_name)
        for item in data:
            items_collection[item.carrier_id] = {}
            items_collection[item.carrier_id]['thickness'] = item.thickness
            items_collection[item.carrier_id]['msl'] = item.msl
            items_collection[item.carrier_id]['hours_greater_than_72'] = item.hours_greater_than_72
            items_collection[item.carrier_id]['hours_less_then_72'] = item.hours_less_72_hours
            items_collection[item.carrier_id]['drying_start_interval'] = item.drying_start_interval



        db_session.close()

        return items_collection
