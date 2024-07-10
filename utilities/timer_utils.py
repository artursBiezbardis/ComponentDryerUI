from datetime import datetime


class TimerUtilities:

    def check_db_item_finished(self, item):
        result = self.time_left_db(item)
        if result <= 0:
            return True
        return False

    @staticmethod
    def time_left(item):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(item['start_time']), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item['drying_start_interval']) + int(item['add_interval']))

        return total_interval_sec - interval_now_sec

    @staticmethod
    def time_left_db(item):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        start_time = datetime.strptime(str(item.start_time), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item.drying_start_interval) + int(item.add_interval))

        return total_interval_sec - interval_now_sec


    @staticmethod
    def calculate_interval(last_activity_date_time):
        time_now = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        last_activity = datetime.strptime(str(last_activity_date_time), "%Y-%m-%d %H:%M:%S.%f")
        interval_now = time_now - last_activity

        return interval_now.total_seconds()
