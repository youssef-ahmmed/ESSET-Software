from models.entities.uart_protocol import Uart
from models import storage
from models.dto.uart_protocol_dto import UartProtocolDto


class UartProtocolDao:
    def __init__(self, uart_protocol_dto: UartProtocolDto):
        self.uart_protocol_dto = uart_protocol_dto
        self.uart = Uart()

        self.create_uart_protocol()

    def create_uart_protocol(self):
        self.uart.sniffed_data_id = self.uart_protocol_dto.sniffed_data_id
        self.uart.clk_per_bit = self.uart_protocol_dto.clk_per_bit
        self.uart.baud_rate = self.uart_protocol_dto.baud_rate
        self.uart.data_size = self.uart_protocol_dto.data_size
        self.uart.stop_bit = self.uart_protocol_dto.stop_bit
        self.uart.parity_bit = self.uart_protocol_dto.parity_bit
        self.uart.significant_bit = self.uart_protocol_dto.significant_bit

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(Uart, id)

    @staticmethod
    def get_all():
        return storage.list_all(Uart)

    def insert(self):
        storage.insert(self.uart)
        storage.save()

    def delete(self):
        storage.delete(self.uart)
        storage.save()

    def update(self, id, clk_per_bit: int, baud_rate: int, data_size: int, stop_bit: int, parity_bit: str,
               significant_bit: str):
        uart_protocol_record: Uart = self.get_by_id(id)
        if uart_protocol_record:
            uart_protocol_record.uart.clk_per_bit = clk_per_bit
            uart_protocol_record.uart.baud_rate = baud_rate
            uart_protocol_record.uart.data_size = data_size
            uart_protocol_record.uart.stop_bit = stop_bit
            uart_protocol_record.uart.parity_bit = parity_bit
            uart_protocol_record.uart.significant_bit = significant_bit

        storage.save()
