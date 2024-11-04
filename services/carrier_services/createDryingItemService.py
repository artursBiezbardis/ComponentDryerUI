from database import AsyncSessionLocal
from repositories.sql_lite_repositories.carrierDataRepository import CarrierDataRepository
from constants import ITEM_DATA_TEMPLATE


class CreateDryingItemService:

    def __init__(self, add_carrier):
        self.add_carrier = add_carrier
        self.item_template = ITEM_DATA_TEMPLATE.copy()

    async def main(self):

        self.item_template['carrier_barcode'] = self.add_carrier['carrier_barcode']
        self.item_template['carrier_position'] = self.add_carrier['carrier_position']
        async with AsyncSessionLocal() as db_session:
            carrier_repo = CarrierDataRepository(db_session)
            self.item_template['part_name'] = await carrier_repo.get_carrier_data(self.add_carrier['carrier_barcode'])['part_name']
        return self.item_template
