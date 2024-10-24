from sqlalchemy.ext.asyncio import AsyncSession
from models.models import TaskData
from datetime import datetime


class TaskDataRepository:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def add_new_task(self, task_template):
        new_task = TaskData(
            carrier_id=task_template['carrier_barcode'],
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
        await self.session.commit()
        await self.session.refresh(new_task)
        task_template['task_id'] = new_task.id
        return task_template

    async def update_finished_task(self, barcode):
        task = await self.session.execute(
            self.session.query(TaskData).filter(TaskData.carrier_id == barcode, TaskData.in_dryer == True)
        )
        task = task.scalar_one_or_none()
        if task:
            task.end_time = datetime.now()
            task.in_dryer = False
            task.drying_finished = True
            await self.session.commit()

    async def get_all_drying_items(self):
        return await self.session.execute(
            self.session.query(TaskData).filter(TaskData.in_dryer == True)
        )

    async def get_all_items(self):
        return await self.session.execute(
            self.session.query(TaskData).all()
        )

    async def update_add_time(self, carrier_id, add_interval):
        task = await self.session.execute(
            self.session.query(TaskData).filter(TaskData.carrier_id == carrier_id, TaskData.in_dryer == True)
        )
        task = task.scalar_one_or_none()
        if task:
            task.add_interval = add_interval
            await self.session.commit()

    async def delete_task_by_id(self, task_id: int):
        task_to_delete = await self.session.get(TaskData, task_id)
        await self.session.delete(task_to_delete)
        await self.session.commit()
