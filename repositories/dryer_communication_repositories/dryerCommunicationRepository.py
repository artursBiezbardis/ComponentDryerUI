import serial
from config import SERIAL_SETTINGS


class SerialManager:
    def __init__(self):
        self.port = SERIAL_SETTINGS['port']
        self.baud_rate = SERIAL_SETTINGS['baud_rate']
        self.timeout = SERIAL_SETTINGS['timeout']
        self.status_request_value = SERIAL_SETTINGS['status_request']
        self.connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def send_data(self, data):
        if self.connection:
            self.connection.write(data.encode()+b'\n')

    def receive_data(self):
        if self.connection:
            data = self.connection.readline().decode().strip()
            return data

    def request(self, request_value):
        if self.connection:
            self.send_data(request_value)


