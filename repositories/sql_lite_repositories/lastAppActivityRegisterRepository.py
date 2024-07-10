from sqlalchemy.orm import Session
from models.models import ActivityRegister
from datetime import datetime


class LastAppActivityRegisterRepository:
    def __init__(self, db_session: Session):
        self.session = db_session
        self.session.close()
        self.session = db_session

    def update_time_now(self):
        time = self.session.query(ActivityRegister).filter(ActivityRegister.id == 1).first()
        if time:
            time.time = datetime.now()
        else:
            time = ActivityRegister(time=datetime.now())

        self.session.add(time)
        self.session.commit()
        self.session.close()

    def get_time(self):
        time = self.session.query(ActivityRegister).filter(ActivityRegister.id == 1).first()
        last_time = time.time
        self.session.close()
        return last_time
