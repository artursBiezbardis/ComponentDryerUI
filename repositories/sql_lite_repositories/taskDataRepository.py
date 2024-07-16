from sqlalchemy.orm import Session
from models.models import TaskData
from datetime import datetime


class TaskDataRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def add_new_task(self, task_template):

        new_task = TaskData(carrier_id=task_template['carrier_barcode'],
                            part_name=task_template['part_name'],
                            carrier_position=task_template['carrier_position'],
                            in_dryer=task_template['in_dryer'],
                            thickness=task_template['part_thickness'],
                            msl=task_template['msl'],
                            hours_less_72_hours=task_template['hours_less_72_hours'],
                            hours_greater_than_72=task_template['hours_greater_than_72'],
                            drying_start_interval=float(task_template['drying_start_interval']) * 3600,
                            add_interval='0',
                            drying_finished=task_template['drying_finished'],
                            start_time=datetime.now(),
                            )

        self.session.add(new_task)
        self.session.commit()
        task_template['task_id'] = new_task.id

        return task_template

    def update_finished_task(self, barcode):
        task = self.session.query(TaskData).filter(TaskData.carrier_id == barcode, TaskData.in_dryer == True).first()
        if task:
            task.end_time = datetime.now()
            task.in_dryer = False
            task.drying_finished = True
            self.session.commit()
            print(f"Row with id {id} updated successfully.")
        else:
            print(f"No row found with id {id}.")

    def get_all_drying_items(self):
        return self.session.query(TaskData).filter(TaskData.in_dryer == True).all()

    def get_all_items(self):
        return self.session.query(TaskData).all()

    def update_add_time(self, carrier_id, add_interval):
        task = self.session.query(TaskData).filter(TaskData.carrier_id == carrier_id, TaskData.in_dryer == True).first()
        if task:
            task.add_interval = add_interval
            self.session.commit()

    def get_all_part_msl_data(self, part_name):

        task_results = self.session.query(TaskData).filter(TaskData.part_name == part_name).all()
        unique_results = self._apply_unique_strategy(task_results)
        return unique_results

    def _apply_unique_strategy(self, results):
        seen = set()
        unique_results = []
        for row in results:
            identifier = (
                row.thickness,
                row.msl,
                row.hours_less_72_hours,
                row.hours_greater_than_72,
                row.drying_start_interval,
                row.msl
            )
            if identifier not in seen:
                seen.add(identifier)
                unique_results.append(row)

        return unique_results
