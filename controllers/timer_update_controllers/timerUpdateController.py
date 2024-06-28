from services.timer_update_services.timerUpdateService import TimerUpdateService


class TimerUpdateController:

    def __init__(self, dryer_status: bool):
        self.dryer_status = dryer_status

    def main(self):

        TimerUpdateService(self.dryer_status).main()

