from services.timer_update_services.timerUpdateService import TimerUpdateService


class TimerUpdateController:

    def __init__(self):
        pass

    def main(self):

        TimerUpdateService(dryer_status=True).main()

