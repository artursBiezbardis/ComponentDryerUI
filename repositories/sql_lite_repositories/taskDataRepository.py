from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
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
        return task_template

    async def reset_finished_task(self, item_id):
        task = await self.session.execute(
            select(TaskData).filter(TaskData.id == item_id, TaskData.in_dryer == True)
        )
        task = task.scalar_one_or_none()
        if task:
            task.end_time = None
            task.drying_finished = False
            await self.session.commit()

    async def update_finished_task(self, barcode):
        task = await self.session.execute(
            select(TaskData).filter(TaskData.carrier_id == barcode, TaskData.in_dryer == True)
        )
        task = task.scalar_one_or_none()
        if task:
            task.end_time = datetime.now()
            task.in_dryer = False
            task.drying_finished = True
            await self.session.commit()

    async def get_all_drying_items(self):

        components_in_dryer = select(TaskData).filter(TaskData.in_dryer == True)
        results = await self.session.execute(components_in_dryer)
        return results.scalars().all()

    async def get_all_items(self):

        results = await self.session.execute(
            select(TaskData))
        return results.scalars().all()

    async def update_add_time(self, id, add_interval):
        task = await self.session.execute(
            select(TaskData).filter(TaskData.id == id, TaskData.in_dryer == True)
        )
        task = task.scalar_one()
        if task:
            task.add_interval = add_interval
            await self.session.commit()

    async def get_all_part_msl_data(self, part_name):
        task_results = await self.session.execute(select(TaskData).filter(TaskData.part_name == part_name))
        task_results = task_results.scalars().all()
        unique_results = self._apply_unique_strategy(task_results)
        return unique_results

    async def delete_task_by_id(self, task_id: int):
        item = select(TaskData).where(TaskData.id == task_id)
        result = await self.session.execute(item)
        task_to_delete = result.scalar_one_or_none()

        if task_to_delete:
            await self.session.delete(task_to_delete)
            await self.session.commit()

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
