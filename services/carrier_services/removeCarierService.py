from database import SessionLocal
from repositories.taskDataRepository import TaskDataRepository
from constants import ITEM_DATA_TEMPLATE, ADD_REM0VE_CARRIER


class RemoveCarrierService:

    def __init__(self, remove_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.remove_carrier = remove_carrier
        self.barcode = barcode
        self.drying_carrier_collection = drying_carrier_collection

    def main(self):
        db_session = SessionLocal()
        carrier_repo = TaskDataRepository(db_session)
        carrier_repo.update_finished_task(self.barcode)
        self.remove_carrier = ADD_REM0VE_CARRIER.copy()
        self.remove_carrier['status_message'] = 'Carrier ' + self.remove_carrier['carrier_barcode'] + ' is in Dryer!!'
        self.set_remove_status()
        db_session.close()
        return self.remove_carrier

    def set_remove_status(self):
        self.remove_carrier['add_status'] = False
        self.remove_carrier['remove_status'] = True
