from services.timer_update_services.timerUpdateService import TimerUpdateService
from repositories.sql_lite_repositories.taskDataRepository import TaskDataRepository

def main():
    i = 0
    while i == 5:
        TimerUpdateService(True, 60).main()
        i = + 1

