from datetime import datetime


class TimerUtilities:

    @staticmethod
    def check_db_item_finished(item):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(item.start_time), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item.drying_start_interval) + int(item.add_interval))
        result = total_interval_sec - interval_now_sec
        if result <= 0:
            return True
        return False
