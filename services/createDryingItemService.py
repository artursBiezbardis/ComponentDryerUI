from database import SessionLocal
from repositories.carrierDataRepository import CarrierDataRepository
from repositories.taskDataRepository import TaskDataRepository


class CreateDryingItemService:

    def __init__(self, add_carrier):
        self.add_carrier = add_carrier
        self.item_template = {'carrier_barcode': self.add_carrier['carrier_barcode'],
                              'carrier_position': self.add_carrier['carrier_position'],
                              'part_name': '',
                              'part_thickness': None,
                              'msl': None,
                              'time_after_72_hours': False,
                              'time_before_72_hours': False,
                              'drying_start_interval': None,
                              'add_interval': None,
                              'in_dryer': True,
                              'drying_finished': False,
                              'task_id': None,
                              'msl_drying_time': None,
                              'start_time': None,
                              'end_time': None,
                              'total_time': None

                              }

    def main(self):
        db_session = SessionLocal()
        carrier_repo = CarrierDataRepository(db_session)
        task_repo = TaskDataRepository(db_session)
        self.item_template['part_name'] = carrier_repo.get_carrier_data(self.add_carrier['carrier_barcode'])['part_name']
        primary_key = task_repo.add_new_task(self.item_template)
        self.item_template['task_id'] = primary_key

        db_session.close()
        return self.item_template
