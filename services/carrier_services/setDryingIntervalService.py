from database import SessionLocal
from repositories.sql_lite_repositories.mslDataRepository import MslDataRepository


class SetDryingIntervalService:

    def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):
        db_session = SessionLocal()
        db_session.close()
        db_session = SessionLocal()
        carrier_repo = MslDataRepository(db_session)
        interval = str(carrier_repo.get_msl_interval(thickness_level, moisture_level, hours_greater_or_less_than_72))
        db_session.close()

        return interval
