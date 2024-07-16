from datetime import datetime


class TimerUtilities:
    def __init__(self):

        self.dt_format = "%Y-%m-%d %H:%M:%S.%f"
    def check_db_item_finished(self, item):
        result = self.time_left_db(item)
        if result <= 0:
            return True
        return False

    def time_left(self, item):
        if not self.check_datetime_format(str(item['start_time']), self.dt_format):
            dt = datetime.fromtimestamp(item['start_time'])
            item['start_time'] = dt.strftime(self.dt_format)
        if item['in_dryer']:
            time_now = datetime.strptime(str(datetime.now()), self.dt_format)
        else:
            time_now = item['end_time']
        # time_now = datetime.strptime(str(datetime.now()), self.dt_format)
        start_time = datetime.strptime(str(item['start_time']), self.dt_format)
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item['drying_start_interval']) + int(item['add_interval']))

        return total_interval_sec - interval_now_sec


    def time_left_db(self,item):
        time_now = datetime.strptime(str(datetime.now()), self.dt_format)
        start_time = datetime.strptime(str(item.start_time), self.dt_format)
        interval_now = time_now - start_time
        interval_now_sec = interval_now.total_seconds()
        total_interval_sec = (int(item.drying_start_interval) + int(item.add_interval))

        return total_interval_sec - interval_now_sec


    def calculate_interval(self,last_activity_date_time):
        time_now = datetime.strptime(str(datetime.now()), self.dt_format)
        last_activity = datetime.strptime(str(last_activity_date_time), self.dt_format)
        interval_now = time_now - last_activity

        return interval_now.total_seconds()

    @staticmethod
    def check_datetime_format(date_string, date_format):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
