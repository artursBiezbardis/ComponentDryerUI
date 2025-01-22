from database import AsyncSessionLocal
from repositories.sql_lite_repositories.carrierDataRepository import CarrierDataRepository
from config import BARCODE_SETTINGS
from utilities.regex_utilities import RegexUtilities
import re


class AddCarrierService:

    def __init__(self, add_carrier: dict, drying_carrier_collection: dict, barcode: str):
        self.add_carrier = add_carrier.copy()
        self.barcode = barcode.lower()
        self.drying_carrier_collection = drying_carrier_collection
        self.item_barcode_regex_pattern = RegexUtilities().create_item_barcode_regex_pattern()

    async def main(self):
        async with AsyncSessionLocal() as db_session:
            carrier_repo = CarrierDataRepository(db_session)
            no_barcodes = ''
            self.add_carrier['alert_message'] = False
            if not self.barcode:
                self.add_carrier['carrier_position'] = ''
                self.add_carrier['alert_message'] = True
                self.add_carrier['status_message'] = f'Enter Barcode'
            elif (self.barcode[0]).lower() in BARCODE_SETTINGS['allowed_first_chars_position_in_dryer'] and len(self.barcode) == BARCODE_SETTINGS['allowed_count_of_chars_position']:
                self.add_carrier['carrier_position'] = self.barcode
                self.add_carrier['status_message'] = f'Dryer position {self.barcode} is set.'
            elif bool(re.match(self.item_barcode_regex_pattern, self.barcode)):
                self.add_carrier['carrier_barcode'] = self.barcode
                carrier_exist = carrier_repo.check_carrier_exist(self.barcode)
                if not carrier_exist:
                    self.add_carrier['message_dismiss_button'] = True
                    self.add_carrier['message_ok_button'] = True
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
