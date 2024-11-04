from database import AsyncSessionLocal
from repositories.sql_lite_repositories.mslDataRepository import MslDataRepository


class MslSelectionValueService:

    async def main(self, thickness):
        async with AsyncSessionLocal() as db_session:
            carrier_repo = MslDataRepository(db_session)
            data = await carrier_repo.filter_msl_for_thickness_values(thickness)
            msl_list = []

            for item in data:
                if item.hours_less_than_72 > 0.0 or item.hours_greater_than_72 > 0.0:
                    msl_list.append(item.moisture_level)


            return msl_list

