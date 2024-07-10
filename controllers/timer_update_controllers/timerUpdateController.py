from services.timer_update_services.timerUpdateService import TimerUpdateService


class TimerUpdateController:

    def __init__(self, dryer_status: bool, add_interval_value: int):
        self.dryer_status = dryer_status
        self.add_interval_value = add_interval_value

    def main(self):

        TimerUpdateService(self.dryer_status, self.add_interval_value).main()

