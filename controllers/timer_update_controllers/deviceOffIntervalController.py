from repositories.sql_lite_repositories.lastAppActivityRegisterRepository import LastAppActivityRegisterRepository
from database import SessionLocal
from utilities.timer_utils import TimerUtilities


class DeviceOffIntervalController:

    def main(self):
        db_session = SessionLocal()
        db_session.close()
        db_session = SessionLocal()
        last_time_on = LastAppActivityRegisterRepository(db_session).get_time()

        return TimerUtilities().calculate_interval(last_time_on)

