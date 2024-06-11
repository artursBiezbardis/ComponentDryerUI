import serial
from utilities.serial_utils import find_available_ports

class SerialManager:
    def __init__(self, port=None, baudrate=9600):
        self.port = port if port else find_available_ports()[0]
        self.baudrate = baudrate
        self.connection = None
    def connect(self):
        if self.port:
            self.connection = serial.Serial(self.port, self.baudrate)
            print(f"Connected to {self.port} at {self.baudrate} baud")
        else:
            raise ValueError("No serial port specified or found")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected")

    def send_data(self, data):
        if self.connection:
            self.connection.write(data.encode())
            print(f"Sent: {data}")
        else:
            raise ConnectionError("Not connected to any serial port")

    def receive_data(self):
        if self.connection:
            data = self.connection.readline().decode()
            print(f"Received: {data}")
            return data
        else:
            raise ConnectionError("Not connected to any serial port")
