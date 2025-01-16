from controllers.carrier_controllers.setDryingIntervalController import SetDryingIntervalController
from controllers.carrier_controllers.startDryingController import StartDryingController
from constants import MSL_EXPIRE
import datetime


class AutoStartDryingService:

    def __init__(self, main_layout):
        self.main_layout = main_layout

    def main(self):

        if self.main_layout.item_data_template['auto_add_task']:
            dt_format = "%Y-%m-%d %H:%M:%S.%f"
            date_time = datetime.datetime
            time_now = (date_time.now()).timestamp()
            pauses = float(self.main_layout.item_data_template['carrier_data']['pauses_total_time']) * 86400
            msl_time = float(self.main_layout.item_data_template['carrier_data']['msl_time']) * 86400
            high_msl_over_time = float(72*60*60)

            time_first_load = float(date_time.strptime(self.main_layout.item_data_template['carrier_data']['time_first_load'], dt_format).timestamp())
            self.main_layout.item_data_template['msl'] = MSL_EXPIRE[int(self.main_layout.item_data_template['carrier_data']['msl_time'])]
            if 500 > int(self.main_layout.item_data_template['carrier_data']['part_height']):
                self.main_layout.item_data_template['part_thickness'] = '< 0.5'
            elif 500 <= int(self.main_layout.item_data_template['carrier_data']['part_height']) < 800:
                self.main_layout.item_data_template['part_thickness'] = '0.8 => 0.5mm'
            elif 800 <= int(self.main_layout.item_data_template['carrier_data']['part_height']) < 1400:
                self.main_layout.item_data_template['part_thickness'] = '1.4 => 0.8mm'
            elif 1400 <= int(self.main_layout.item_data_template['carrier_data']['part_height']) < 2000:
                self.main_layout.item_data_template['part_thickness'] = '2 => 1.4mm'
            elif 2000 <= int(self.main_layout.item_data_template['carrier_data']['part_height']) < 4500:
                self.main_layout.item_data_template['part_thickness'] = '4.5 => 2mm'

            if time_now - time_first_load - pauses - msl_time > high_msl_over_time:
                self.main_layout.item_data_template['hours_greater_than_72'] = True
                self.main_layout.item_data_template['hours_less_72_hours'] = False
                hours_less_greater = 'hours greater than 72'
            else:
                self.main_layout.item_data_template['hours_greater_than_72'] = False
                self.main_layout.item_data_template['hours_less_72_hours'] = True
                hours_less_greater = 'hours less 72 hours'

            msl_interval = SetDryingIntervalController()
            self.main_layout.item_data_template['drying_start_interval'] = msl_interval.main(
                self.main_layout.item_data_template['part_thickness'],
                self.main_layout.item_data_template['msl'],
                hours_less_greater)

            start_drying = StartDryingController()
            self.main_layout.last_action_info = 'Carrier '+self.main_layout.item_data_template['carrier_barcode']+' is added to dryer'
            self.main_layout.set_last_action_info()
            start_drying.main(self.main_layout.item_data_template)
