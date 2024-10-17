from services.dryer_alarm_services.dryerAlarmService import DryerAlarmService
class DryerAlarmController:

    def main(self):

        alarm_data = DryerAlarmService().main()

        return alarm_data
