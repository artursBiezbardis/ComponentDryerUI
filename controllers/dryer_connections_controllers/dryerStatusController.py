import serial
from .serial_utils import find_available_ports

class SerialManager:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        self.connection = serial.Serial(self.port, self.baudrate)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def send_data(self, data):
        if self.connection:
            self.connection.write(data.encode())

    def receive_data(self):
        if self.connection:
            return self.connection.readline().decode()