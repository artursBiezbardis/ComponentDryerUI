from database import AsyncSessionLocal
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository
from constants import ADD_REM0VE_CARRIER
from utilities.timer_utils import TimerUtilities
from services.tpsys_services.updateTpsysCarrierTimeService import UpdateTpsysCarrierTimeService
from repositories.sql_lite_repositories.carrierDataRepository import CarrierDataRepository


class RemoveCarrierService:

    def __init__(self, remove_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.remove_carrier = remove_carrier
        self.barcode = barcode
        self.drying_carrier_collection = drying_carrier_collection

    async def main(self):
        if not self.check_if_carrier_finished() and not self.remove_carrier['on_enter_recycle']:
            self.remove_carrier['add_status'] = False
            self.remove_carrier['remove_status'] = False
            self.remove_carrier['message_dismiss_button'] = True
            self.remove_carrier['message_ok_button'] = True
            self.remove_carrier['status_message'] = 'Carrier ' + self.remove_carrier[
                'carrier_barcode'] + ' is not Finished!\nDO YOU WANT TO REMOVE ITEM'
            self.remove_carrier['alert_message'] = True
            self.remove_carrier['on_enter_recycle'] = True
            self.remove_carrier['carrier_barcode'] = self.barcode
        else:
            async with AsyncSessionLocal() as db_session:
                task_repo = TaskDataRepository(db_session)
                await task_repo.update_finished_task(self.barcode)
                self.remove_carrier = ADD_REM0VE_CARRIER.copy()
                self.remove_carrier['status_message'] = 'Carrier ' + self.remove_carrier['carrier_barcode'] + ' removed from Dryer!!'
                self.set_remove_status()
                self.remove_carrier['on_enter_recycle'] = False
                async with AsyncSessionLocal() as db_session:
                    carrier_repo = CarrierDataRepository(db_session)
                    carrier_exist = await carrier_repo.check_carrier_exist(self.barcode)
                    if carrier_exist:
                        remote_update = UpdateTpsysCarrierTimeService(self.barcode).main()
                        if not remote_update:
                            self.remove_carrier['status_message'] = self.remove_carrier['status_message'] + '\nRemote DB is\'t updated!!!'
                            self.remove_carrier['alert_message'] = True

        return self.remove_carrier

    def set_remove_status(self):
        self.remove_carrier['add_status'] = False
        self.remove_carrier['remove_status'] = True

    def check_if_carrier_finished(self):
        result = False
        if TimerUtilities().time_left(self.drying_carrier_collection[self.barcode]) <= 0:
            result = True
        return result
