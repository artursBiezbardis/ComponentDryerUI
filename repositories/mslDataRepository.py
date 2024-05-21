from sqlalchemy.orm import Session
from models.models import MslData


class MslDataRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def get_msl_time(self, thickness_level, moisture_level, hours_greater_or_less_than_72):

        data = self.session.query(MslData).filter(MslData.thickness_level == thickness_level, MslData.moisture_level == moisture_level).first()
        test = data
        selector = hours_greater_or_less_than_72.replace(" ", "_")
        test = data.selector

        return data[selector]

