from models.models import CarrierData
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class CarrierDataRepository:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def check_carrier_exist(self, barcode: str) -> bool:
        db_barcode = barcode
        db_barcode = db_barcode[1:]
        result = False
        data = await self.session.execute(select(CarrierData).filter(CarrierData.carrier_id == db_barcode))
        data_val = data.scalars().first()
        if data_val:
            result = True
        return result

    async def get_carrier_data(self, barcode: str):
        db_barcode = barcode
        db_barcode = db_barcode[1:]
        data = await self.session.execute(select(CarrierData).filter(CarrierData.carrier_id == db_barcode))
        data_val = data.scalars().first()
        if not data_val:
            return {'id': None, 'carrier_id': barcode, 'part_name': None}
        return {
            'id': data_val.id,
            'carrier_id': data_val.carrier_id,
            'part_name': data_val.part_name,
            'quantity': data_val.quantity,
            'time_first_load': data_val.time_first_load,
            'msl_time': data_val.msl_time,
            'pauses_total_time': data_val.pauses_total_time,
            'part_height': data_val.part_height
        }
