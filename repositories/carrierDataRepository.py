from models.models import CarrierData, Session


class CarrierDataRepository:

    @staticmethod
    def check_carrier_exist(barcode: str) -> bool:
        db_barcode = barcode
        db_barcode = db_barcode[1:]
        result = False
        session = Session()
        data = session.query(CarrierData).filter(CarrierData.carrier_id == db_barcode).first()
        if data:
            result = True
        return result
