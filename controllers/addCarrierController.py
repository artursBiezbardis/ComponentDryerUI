import repositories.carrierDataRepository as repo


class AddCarrierController:

    def __init__(self, add_carrier: dict, barcode: str):
        self.add_carrier = add_carrier
        self.barcode = barcode

    def main(self):
        no_barcodes = ''
        if (self.barcode[0]).lower() == 'l' and len(self.barcode) == 3:
            self.add_carrier['carrier_position'] = self.barcode
            self.add_carrier['status_message'] = f'Dryer position {self.barcode} is set.'
        elif (self.barcode[0]).lower() == 'r' and len(self.barcode) == 7:
            self.add_carrier['carrier_barcode'] = self.barcode
            if repo.CarrierDataRepository().check_carrier_exist(self.barcode):
                no_barcodes = f'This barcode is not registered!!!!!'
            self.add_carrier['status_message'] = f'Carrier {self.barcode} is set.{no_barcodes}'
        else:
            self.add_carrier['status_message'] = f'Not valid barcode'

        return self.add_carrier
