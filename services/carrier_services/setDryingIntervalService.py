from database import AsyncSessionLocal
from repositories.sql_lite_repositories.mslDataRepository import MslDataRepository


class SetDryingIntervalService:

    async def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):
        async with AsyncSessionLocal() as db_session:
            carrier_repo = MslDataRepository(db_session)
            interval = await carrier_repo.get_msl_interval(thickness_level, moisture_level, hours_greater_or_less_than_72)

        return str(interval)
