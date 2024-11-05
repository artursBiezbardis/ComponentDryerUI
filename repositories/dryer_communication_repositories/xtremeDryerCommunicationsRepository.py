import json
import os
import time
import config


class XtremeDryerCommunicationsRepository:

    @staticmethod
    def main():
        cwd = os.getcwd()
        expected_path = os.path.join(cwd, 'liveMonitorData.json')
        new_modified_time = os.path.getmtime(expected_path)
        time_now = time.time()
        if config.TIMER_SETTINGS['json_read_lower_offset'] < (time_now - new_modified_time) > config.TIMER_SETTINGS['json_read_higher_offset']:
            time.sleep(1.1)
        try:
            with open(expected_path, 'r') as liveMonitorData:
                dryer_data_now = json.load(liveMonitorData)
        except Exception as e:
            with open(expected_path, 'r') as liveMonitorData:
                dryer_data_now = {'door1_closed': True, 'door2_closed': True, 'last_alarm': '', 'on_line': True, 'rh_value': 0.78, 'set_rh': 0.5, 'set_temp': 20.0, 'temp_value': 23.8, 'time': time_now}

        return dryer_data_now
