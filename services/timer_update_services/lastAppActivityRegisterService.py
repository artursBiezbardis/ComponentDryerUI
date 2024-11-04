from database import AsyncSessionLocal
from repositories.sql_lite_repositories.lastAppActivityRegisterRepository import LastAppActivityRegisterRepository


class LastAppActivityRegisterService:

    async def main(self):
        async with AsyncSessionLocal() as db_session:

            await LastAppActivityRegisterRepository(db_session).update_time_now()
