from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import ActivityRegister
from datetime import datetime
import logging


class LastAppActivityRegisterRepository:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def update_time_now(self):
        logging.info("Updating time entry with id == 1")

        result = await self.session.execute(
            select(ActivityRegister).filter(ActivityRegister.id == 1)
        )
        time_entry = result.scalars().first()

        if time_entry:
            time_entry.time = datetime.now()
            await self.session.commit()

    async def get_time(self):
        logging.info("Fetching the last activity time entry")
        result = await self.session.execute(
            select(ActivityRegister).filter(ActivityRegister.id == 1)
        )
        time_entry = result.scalars().first()

        if time_entry:
            logging.info(f"Fetched time: {time_entry.time}")
            return time_entry.time
        else:
            logging.warning("No time entry found with id == 1")
            return None
