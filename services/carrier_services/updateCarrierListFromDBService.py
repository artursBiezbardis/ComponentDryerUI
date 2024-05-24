from constants import ITEM_DATA_TEMPLATE
from database import SessionLocal
from repositories.taskDataRepository import TaskDataRepository


class UpdateCarrierListFromDBService:

    def main(self):
        db_session = SessionLocal()
        db_session.close()
        items_collection = {}
        drying_item = ITEM_DATA_TEMPLATE

        db_session = SessionLocal()
        task_repo = TaskDataRepository(db_session)
        items_in_dryer = task_repo.get_all_drying_items()
        for item in items_in_dryer.values():
            drying_item = ITEM_DATA_TEMPLATE




        db_session.close()

        return items_in_dryer