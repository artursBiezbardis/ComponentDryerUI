from repositories.dryer_communication_repositories.xtremeDryerCommunicationsRepository import XtremeDryerCommunicationsRepository
import time
import config


class XtremeDryerCommunicationsService:

    def main(self):
        dryer_status_output = {'dryer_status': False, 'dryer_status_info': 'no connection'}

        dryer_data_now = XtremeDryerCommunicationsRepository().main()
        humidity = dryer_data_now['rh_value']
        temp = dryer_data_now['temp_value']
        set_humidity = dryer_data_now['set_rh']
        set_temp = dryer_data_now['set_temp']
        humidity_min = set_humidity - config.DRYER_ENV_LIMITS['humidity_min']
        humidity_max = set_humidity + config.DRYER_ENV_LIMITS['humidity_max']
        temp_min = set_temp - config.DRYER_ENV_LIMITS['temp_min']
        temp_max = set_temp + config.DRYER_ENV_LIMITS['temp_max']

        if self.check_connection_timeout(dryer_data_now['time']) and dryer_data_now['on_line']:
            dryer_status_output['dryer_status_info'] = 'RH is too high'
            if humidity_min <= humidity <= humidity_max and temp_min <= temp <= temp_max:
                dryer_status_output['dryer_status_info'] = 'drying active'
                dryer_status_output['dryer_status'] = True

        return dryer_status_output

    @staticmethod
    def check_connection_timeout(live_monitor_data_update_time: float) -> bool:

        max_connection_timeout = config.CONNECTION_TIMEOUT['connection_timeout_for_status']
        time_now = time.time()
        result = True
        if time_now - live_monitor_data_update_time >= max_connection_timeout:
            result = False

        return result
