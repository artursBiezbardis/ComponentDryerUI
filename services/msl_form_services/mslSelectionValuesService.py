from database import SessionLocal
from repositories.mslDataRepository import MslDataRepository


class MslSelectionValueService:

    def main(self, thickness):
        db_session = SessionLocal()
        db_session.close()
        db_session = SessionLocal()
        carrier_repo = MslDataRepository(db_session)
        data = carrier_repo.filter_msl_for_thickness_values(thickness)
        msl_list = []

        for item in data:
            if item.hours_less_than_72 > 0.0 or item.hours_greater_than_72 > 0.0:
                msl_list.append(item.moisture_level)

        db_session.close()

        return msl_list

