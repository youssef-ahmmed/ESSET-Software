import time
import serial.tools.list_ports
from serial.serialutil import SerialException, SerialTimeoutException


class SerialCommunication:
    serial_port = serial.Serial()

    def __init__(self):
        SerialCommunication.start_communication()

    @staticmethod
    def start_communication():
        if not SerialCommunication.serial_port.is_open:
            SerialCommunication.serial_port.open()
        SerialCommunication.get_default_data()

    def execute_serial_transaction(self, data):
        try:
            self.send_data(data)
            print("Transaction successful.")
        except Exception as e:
            print("Error: Port not open.")

    def execute_serial_receiving(self):
        try:
            data = self.read_data()
            print("Receive successful.")
            print(f"Data Received: {data}")
        except Exception as e:
            print("Error: Port not open.")

    @staticmethod
    def get_default_data():
        SerialCommunication.serial_port.port = 'COM1'
        SerialCommunication.serial_port.baudrate = int(9600)
        SerialCommunication.serial_port.bytesize = int(8)
        SerialCommunication.serial_port.parity = 'N'
        SerialCommunication.serial_port.stopbits = int(1)
        SerialCommunication.serial_port.timeout = int(0)

    def send_data(self, data):
        try:
            if not SerialCommunication.serial_port.is_open:
                print("Error: Port not open.")
                return False
            else:
                for char in data:
                    SerialCommunication.serial_port.write(char.encode())
                    time.sleep(0.01)
        except SerialTimeoutException as e:
            print("Error: Timeout.")
            raise e
        except SerialException as e:
            print("Error: Configuration error.")
            raise e

    def read_data(self):
        try:
            received_data = SerialCommunication.serial_port.readline().decode()
            return received_data
        except SerialTimeoutException as e:
            print("Error: Timeout.")
            raise e
        except SerialException as e:
            print("Error: Configuration error.")
            raise e
