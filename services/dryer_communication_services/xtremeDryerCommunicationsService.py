from repositories.dryer_communication_repositories.xtremeDryerCommunicationsRepository import XtremeDryerCommunicationsRepository
import time
import config


class XtremeDryerCommunicationsService:

    def main(self):

        dryer_data_now = XtremeDryerCommunicationsRepository().main()
        humidity = dryer_data_now['rh_value']
        temp = dryer_data_now['temp_value']
        set_humidity = dryer_data_now['set_rh']
        set_temp = dryer_data_now['set_temp']
        humidity_min = set_humidity - config.DRYER_ENV_LIMITS['humidity_min']
        humidity_max = set_humidity + config.DRYER_ENV_LIMITS['humidity_max']
        temp_min = set_temp - config.DRYER_ENV_LIMITS['temp_min']
        temp_max = set_temp + config.DRYER_ENV_LIMITS['temp_max']

        result = False
        if self.check_connection_timeout(dryer_data_now['time']) and dryer_data_now['on_line']:

            if humidity_min <= humidity <= humidity_max and temp_min <= temp <= temp_max:
                result = True

        return result

    @staticmethod
    def check_connection_timeout(live_monitor_data_update_time: float) -> bool:

        max_connection_timeout = config.CONNECTION_TIMEOUT['connection_timeout_for_status']
        time_now = time.time()
        result = True
        if time_now - live_monitor_data_update_time >= max_connection_timeout:
            result = False

        return result
