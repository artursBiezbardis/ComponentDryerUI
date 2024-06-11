from database import SessionLocal
from repositories.sql_lite_repositories.carrierDataRepository import CarrierDataRepository
from constants import ITEM_DATA_TEMPLATE


class CreateDryingItemService:

    def __init__(self, add_carrier):
        self.add_carrier = add_carrier
        self.item_template = ITEM_DATA_TEMPLATE

    def main(self):

        self.item_template['carrier_barcode'] = self.add_carrier['carrier_barcode']
        self.item_template['carrier_position'] = self.add_carrier['carrier_position']
        db_session = SessionLocal()
        carrier_repo = CarrierDataRepository(db_session)
        self.item_template['part_name'] = carrier_repo.get_carrier_data(self.add_carrier['carrier_barcode'])['part_name']
        db_session.close()
        return self.item_template
