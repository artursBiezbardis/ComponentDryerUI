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
            time.sleep(1)
            print(time_now - new_modified_time)
        try:
            with open(expected_path, 'r') as liveMonitorData:
                dryer_data_now = json.load(liveMonitorData)
        except Exception as e:
            print(time_now - new_modified_time,{e})
            time.sleep(0.5)
            with open(expected_path, 'r') as liveMonitorData:
                dryer_data_now = json.load(liveMonitorData)

        return dryer_data_now
