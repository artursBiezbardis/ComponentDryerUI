from database import SessionLocal
from repositories.sql_lite_repositories.carrierDataRepository import CarrierDataRepository


class AddCarrierService:

    def __init__(self, add_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.add_carrier = add_carrier.copy()
        self.barcode = barcode
        self.drying_carrier_collection = drying_carrier_collection

    def main(self):
        db_session = SessionLocal()
        carrier_repo = CarrierDataRepository(db_session)
        no_barcodes = ''
        self.add_carrier['alert_message'] = False
        if not self.barcode:
            self.add_carrier['carrier_position'] = ''
            self.add_carrier['alert_message'] = True
            self.add_carrier['status_message'] = f'Enter Barcode'
        elif (self.barcode[0]).lower() == 'l' and len(self.barcode) == 4:
            self.add_carrier['carrier_position'] = self.barcode
            self.add_carrier['status_message'] = f'Dryer position {self.barcode} is set.'
        elif (self.barcode[0]).lower() == 'r' and len(self.barcode) == 7:
            self.add_carrier['carrier_barcode'] = self.barcode
            if not carrier_repo.check_carrier_exist(self.barcode):
                self.add_carrier['alert_message'] = True
                no_barcodes = f'This barcode is not registered!!!!!'
            self.add_carrier['status_message'] = f'Carrier {self.barcode} is set.{no_barcodes}'
        else:
            self.add_carrier['alert_message'] = True
            self.add_carrier['status_message'] = f'Not valid barcode'
        self.set_add_status()
        return self.add_carrier

    def set_add_status(self):
        if self.add_carrier['carrier_barcode'] and self.add_carrier['carrier_position']:
            self.add_carrier['add_status'] = True
            self.add_carrier['remove_status'] = False
