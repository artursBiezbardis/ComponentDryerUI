import serial
from config import SERIAL_SETTINGS
import time

class SerialManager:
    def __init__(self, layout):
        self.port = SERIAL_SETTINGS['port']
        self.baud_rate = SERIAL_SETTINGS['baud_rate']
        self.timeout = SERIAL_SETTINGS['timeout']
        self.status_request_value = SERIAL_SETTINGS['status_request']
        self.connection_active = False
        self.layout = layout
        self.connection = self.connecting()


    def disconnect(self):
        if self.connection:
            self.connection.close()

    def send_data(self, data):
        if self.connection.is_open:
            try:
                self.connection.write(data.encode() + b'\n')
            except serial.SerialTimeoutException:
                print(f'Write timeout on {self.port}')

    def receive_data(self):
        if self.connection:
            data = self.connection.readline().decode().strip()
            return data

    def request(self, request_value):
        if self.connection:
            self.send_data(request_value)

    def connecting(self):
        while not self.connection_active:

            loop_indicator_count = 0
            connection_loop_indicator = ''
            try:
                ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
                if ser.is_open:
                    self.connection_active = True
                else:
                    self.connection_active = False
                    info_text = f"Failed to open port {self.port}"
                    info_text = info_text + connection_loop_indicator
                    print(info_text)
                    time.sleep(2)
                    if loop_indicator_count <= 10:
                        loop_indicator_count = +1
                    else:
                        loop_indicator_count = 0
                    connection_loop_indicator = self.connection_info_text_update(loop_indicator_count,
                                                                                 connection_loop_indicator)
                    print(info_text+'\n')
                    time.sleep(2)
            except serial.SerialException as e:
                print("Error: " + str(e)+'\n')
                time.sleep(2)
        return ser


    @staticmethod
    def connection_info_text_update(loop_indicator_count, connection_loop_indicator):
        result = connection_loop_indicator
        if (loop_indicator_count % 2) != 0:
            result = result + '.'
        else:
            result = result + ' '

        return result
