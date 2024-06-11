import serial.tools.list_ports


def find_available_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]
