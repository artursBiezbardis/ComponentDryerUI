from constants import ITEM_DATA_TEMPLATE
from database import SessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository


class UpdateCarrierListFromDBService:
    _ITEM_DATA_TEMPLATE = ITEM_DATA_TEMPLATE.copy

    def main(self):
        db_session = SessionLocal()
        db_session.close()
        items_collection = {}
        db_session = SessionLocal()
        task_repo = TaskDataRepository(db_session)
        items_in_dryer = task_repo.get_all_drying_items()
        for item in items_in_dryer:
            items_collection[item.carrier_id] = {}
            items_collection[item.carrier_id]['carrier_barcode'] = item.carrier_id
            items_collection[item.carrier_id]['carrier_position'] = item.carrier_position
            items_collection[item.carrier_id]['part_name'] = item.part_name
            items_collection[item.carrier_id]['part_thickness'] = item.thickness
            items_collection[item.carrier_id]['msl'] = item.msl
            items_collection[item.carrier_id]['hours_greater_than_72'] = item.hours_greater_than_72
            items_collection[item.carrier_id]['hours_less_72_hours'] = item.hours_less_72_hours
            items_collection[item.carrier_id]['drying_start_interval'] = item.drying_start_interval
            items_collection[item.carrier_id]['add_interval'] = item.add_interval
            items_collection[item.carrier_id]['in_dryer'] = item.in_dryer
            items_collection[item.carrier_id]['task_id'] = item.id
            items_collection[item.carrier_id]['start_time'] = item.start_time
            items_collection[item.carrier_id]['end_time'] = item.end_time
            items_collection[item.carrier_id]['total_time'] = item.total_time

        db_session.close()

        return items_collection
