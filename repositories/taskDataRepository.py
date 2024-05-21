from sqlalchemy.orm import Session
from models.models import TaskData


class TaskDataRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def add_new_task(self, task_template):

        new_task = TaskData(carrier_id=task_template['carrier_barcode'][1:],
                            part_name=task_template['part_name'],
                            carrier_position=task_template['carrier_position'],
                            in_dryer=task_template['in_dryer']
                            )
        self.session.add(new_task)
        self.session.commit()
        primary_key = self.session.query(TaskData).filter(
            TaskData.carrier_id == task_template['carrier_barcode'][1:]).first()

        return primary_key.id

    def update_finished_task(self, id_key, new_value):
        # Query for the row by id
        task = self.session.query(TaskData).filter(TaskData.id == id_key).first()
        if task:
            # Update the desired column
            task.your_column = new_value
            # Commit the changes to the database
            self.session.commit()
            print(f"Row with id {id} updated successfully.")
        else:
            print(f"No row found with id {id}.")
