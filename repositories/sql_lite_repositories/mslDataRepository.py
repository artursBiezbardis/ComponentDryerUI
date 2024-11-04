from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import MslData


class MslDataRepository:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def get_msl_interval(self, thickness_level, moisture_level, hours_greater_or_less_than_72):

        data = await self.session.execute(select(MslData).filter(MslData.thickness_level == thickness_level,
                                                           MslData.moisture_level == moisture_level))
        data_val = data.scalars().first()
        result = '0'
        if hours_greater_or_less_than_72 == 'hours greater than 72':
            result = data_val.hours_greater_than_72
        elif hours_greater_or_less_than_72 == 'hours less than 72':
            result = data_val.hours_less_than_72

        return float(result)

    async def filter_msl_for_thickness_values(self, value):

        data = await self.session.execute(select(MslData).filter(MslData.thickness_level == value))
        data = data.scalars().all()
        return data

