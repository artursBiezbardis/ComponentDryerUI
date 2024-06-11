from sqlalchemy.orm import Session
from models.models import CarrierData


class CarrierDataRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def check_carrier_exist(self, barcode: str) -> bool:
        db_barcode = barcode
        db_barcode = db_barcode[1:]
        result = False
        data = self.session.query(CarrierData).filter(CarrierData.carrier_id == db_barcode).first()
        self.session.close()
        if data:
            result = True
        return result

    def get_carrier_data(self, barcode: str):
        db_barcode = barcode
        db_barcode = db_barcode[1:]
        data = self.session.query(CarrierData).filter(CarrierData.carrier_id == db_barcode).first()
        self.session.close_all()
        if not data:
            return {'id': None, 'carrier_id': barcode, 'part_name': None}
        return {'id': data.id, 'carrier_id': data.carrier_id, 'part_name': data.part_name}
