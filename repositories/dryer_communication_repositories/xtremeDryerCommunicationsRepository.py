import json
import os


class XtremeDryerCommunicationsRepository:

    @staticmethod
    def main():
        cwd = os.getcwd()
        expected_path = os.path.join(cwd, 'liveMonitorData.json')

        with open(expected_path, 'r') as liveMonitorData:
            dryer_data_now = json.load(liveMonitorData)

        return dryer_data_now
