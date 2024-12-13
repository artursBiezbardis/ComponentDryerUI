from repositories.dryer_communication_repositories.xtremeDryerCommunicationsRepository import XtremeDryerCommunicationsRepository
import time


class DryerAlarmService:

    def main(self):
        alarm_message = {'alert': False, 'alert_message': ''}

        alert_data = XtremeDryerCommunicationsRepository().main()

        if not self.check_connection_timeout(alert_data['time']):
            alarm_message = {'alert': True, 'alert_message': 'No connection with dryer!\n Check dryer is on or it\'s connected to local network. '}
        elif not alert_data['door1_closed'] and not alert_data['door2_closed']:
            alarm_message = {'alert': True,
                             'alert_message': 'Door 1 and 2 is open!'}
        elif not alert_data['door1_closed']:
            alarm_message = {'alert': True,
                             'alert_message': 'Door 1 is open!'}
        elif not alert_data['door2_closed']:
            alarm_message = {'alert': True,
                             'alert_message': 'Door 2 is open!'}

        return alarm_message

    @staticmethod
    def check_connection_timeout(live_monitor_data_update_time: float) -> bool:

        max_connection_timeout = 10
        time_now = time.time()
        result = True
        if time_now - live_monitor_data_update_time >= max_connection_timeout:
            result = False

        return result
