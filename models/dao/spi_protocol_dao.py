from models.entities.spi_protocol import Spi
from models import storage


class SpiProtocolDAO:
    def __init__(self, spi_protocol_dto):
        self.spi_protocol_dto = spi_protocol_dto
        self.spi = Spi()

        self.create_spi_protocol()

    def create_spi_protocol(self):
        self.spi.sniffed_data_id = self.spi_protocol_dto.sniffed_data_id
        self.spi.significant_bit = self.spi_protocol_dto.significant_bit
        self.spi.clk_state = self.spi_protocol_dto.clk_state
        self.spi.clk_phase = self.spi_protocol_dto.clk_phase
        self.spi.data_size = self.spi_protocol_dto.data_size

    def insert(self):
        storage.insert(self.spi)
        storage.save()

    def delete(self):
        storage.delete(self.spi)
        storage.save()

    def update(self, id, significant_bit, clk_state, clk_phase, data_size):
        spi_protocol_record = storage.get_by_id(Spi, id)
        if spi_protocol_record:
            spi_protocol_record.significant_bit = significant_bit
            spi_protocol_record.clk_state = clk_state
            spi_protocol_record.clk_phase = clk_phase
            spi_protocol_record.data_size = data_size

        storage.save()
