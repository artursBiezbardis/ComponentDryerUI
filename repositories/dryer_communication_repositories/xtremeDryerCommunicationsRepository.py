import json
import os
import time
import config


class XtremeDryerCommunicationsRepository:

    def __init__(self):
        self.cwd = os.getcwd()
        self.expected_path = os.path.join(self.cwd, 'liveMonitorData.json')

    def main(self):
        dryer_data_now = {}
        while not dryer_data_now:
            time.sleep(0.3)
            dryer_data_now = self.read_extracted_data()

        return dryer_data_now

    def read_extracted_data(self):
        try:
            with open(self.expected_path, 'r') as liveMonitorData:
                dryer_data_now = json.load(liveMonitorData)
        except Exception as e:
            print(e)
            return {}

        return dryer_data_now

    @staticmethod
    def get_seconds_and_deci_seconds() -> list:

        time_now = time.time()
        seconds = int(time_now)
        last_digit_sec = seconds % 10
        milliseconds = int((time_now - int(time_now)) * 1000)
        first_digit_milli_seconds = int(str(milliseconds)[0])

        return [last_digit_sec, first_digit_milli_seconds]

