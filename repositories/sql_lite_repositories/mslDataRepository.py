from sqlalchemy.orm import Session
from models.models import MslData
import ast


class MslDataRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def get_msl_interval(self, thickness_level, moisture_level, hours_greater_or_less_than_72):

        data = self.session.query(MslData).filter(MslData.thickness_level == thickness_level, MslData.moisture_level == moisture_level).first()
        result = '0'
        if hours_greater_or_less_than_72 == 'hours greater than 72':
            result = data.hours_greater_than_72
        elif hours_greater_or_less_than_72 == 'hours less than 72':
            result = data.hours_less_than_72

        return float(result)

    def filter_msl_for_thickness_values(self, value):

        data = self.session.query(MslData).filter(MslData.thickness_level == value).all()
        return data

