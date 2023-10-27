from models.entities.uart_protocol import Uart
from models import storage


class UartProtocolDAO:
    def __init__(self, uart_protocol_dto):
        self.uart_protocol_dto = uart_protocol_dto
        self.uart = Uart()

        self.create_uart_protocol()

    def create_uart_protocol(self):
        self.uart.clk_per_bit = self.uart_protocol_dto.clk_per_bit
        self.uart.baud_rate = self.uart_protocol_dto.baud_rate
        self.uart.data_size = self.uart_protocol_dto.data_size
        self.uart.stop_bit = self.uart_protocol_dto.stop_bit
        self.uart.parity_bit = self.uart_protocol_dto.parity_bit


    def insert(self):
        storage.insert(self.uart)
        storage.save()

    def delete(self):
        storage.delete(self.uart)
        storage.save()

    def update(self, id, clk_per_bit, baud_rate, data_size, stop_bit, parity_bit):
        uart_protocol_record = storage.get_by_id(Uart, id)
        if uart_protocol_record:
            uart_protocol_record.uart.clk_per_bit = clk_per_bit
            uart_protocol_record.uart.baud_rate = baud_rate
            uart_protocol_record.uart.data_size = data_size
            uart_protocol_record.uart.stop_bit = stop_bit
            uart_protocol_record.uart.parity_bit = parity_bit

        storage.save()
