import time
import serial.tools.list_ports
from serial.serialutil import SerialException, SerialTimeoutException
from loguru import logger
from models import log_messages


class SerialCommunication:
    serial_port = serial.Serial()

    def __init__(self):
        SerialCommunication.start_communication()

    @staticmethod
    def start_communication():
        SerialCommunication.get_default_data()
        if not SerialCommunication.serial_port.is_open:
            SerialCommunication.serial_port.open()

    def execute_serial_transaction(self, data):
        try:
            self.send_data(data)
            logger.success(log_messages.SENDING_SUCCESS)
        except Exception as e:
            logger.error(log_messages.PORT_NOT_OPEN_ERROR)

    def execute_serial_receiving(self):
        try:
            data = self.read_data()
            logger.success(log_messages.RECEIVE_SUCCESS)
            print(f"Data Received: {data}")
        except Exception as e:
            logger.error(log_messages.PORT_NOT_OPEN_ERROR)

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
                logger.error(log_messages.PORT_NOT_OPEN_ERROR)
                return False
            else:
                for char in data:
                    SerialCommunication.serial_port.write(char.encode())
                    time.sleep(0.01)
        except SerialTimeoutException as e:
            logger.error(log_messages.TIMEOUT_ERROR)
        except SerialException as e:
            logger.error(log_messages.CONFIGURATION_ERROR)

    def read_data(self):
        try:
            received_data = SerialCommunication.serial_port.readline().decode()
            return received_data
        except SerialTimeoutException as e:
            logger.error(log_messages.TIMEOUT_ERROR)
        except SerialException as e:
            logger.error(log_messages.CONFIGURATION_ERROR)
