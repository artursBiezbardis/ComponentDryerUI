from database import SessionLocal
from repositories.sql_lite_repositories.lastAppActivityRegisterRepository import LastAppActivityRegisterRepository


class LastAppActivityRegisterController:

    def main(self):
        db_session = SessionLocal()
        last_app_activity_repo = LastAppActivityRegisterRepository(db_session)
        last_app_activity_repo.update_time_now()

