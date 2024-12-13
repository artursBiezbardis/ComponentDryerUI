from database import AsyncSessionLocal
from repositories.sql_lite_repositories.lastAppActivityRegisterRepository import LastAppActivityRegisterRepository
from utilities.timer_utils import TimerUtilities
from datetime import datetime


class DeviceOffIntervalService:

    async def main(self):

        async with AsyncSessionLocal() as db_session:
            last_time_on = await LastAppActivityRegisterRepository(db_session).get_time()
            if not last_time_on:
                last_time_on = datetime.now()

        return TimerUtilities().calculate_interval(last_time_on)

