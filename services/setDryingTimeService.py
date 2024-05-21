from database import SessionLocal
from repositories.mslDataRepository import MslDataRepository


class SetDryingTimeService:

    def main(self, thickness_level, moisture_level, hours_greater_or_less_than_72):
        db_session = SessionLocal()
        carrier_repo = MslDataRepository(db_session)
        time = carrier_repo.get_msl_time(thickness_level, moisture_level, hours_greater_or_less_than_72)
        db_session.close()

        return time
