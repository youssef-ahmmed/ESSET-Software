from models.entities.sniffed_data import SniffedData
from models.entities.spi_protocol import Spi
from models import storage
from models.dto.spi_protocol_dto import SpiProtocolDto


class SpiProtocolDao:
    def __init__(self, spi_protocol_dto: SpiProtocolDto):
        self.spi_protocol_dto = spi_protocol_dto
        self.spi = Spi()

        self.create_spi_protocol()

    def create_spi_protocol(self):
        self.spi.sniffed_data_id = self.spi_protocol_dto.sniffed_data_id
        self.spi.clock_rate = self.spi_protocol_dto.clock_rate
        self.spi.significant_bit = self.spi_protocol_dto.significant_bit
        self.spi.clk_state = self.spi_protocol_dto.clk_state
        self.spi.clk_phase = self.spi_protocol_dto.clk_phase
        self.spi.data_size = self.spi_protocol_dto.data_size

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(Spi, id)

    @staticmethod
    def get_all():
        return storage.list_all(Spi)

    @staticmethod
    def get_clock_rate_by_start_time(start_time):
        return storage.get_all_by_join(SniffedData, Spi, start_time)[0].clock_rate

    @staticmethod
    def get_clock_rate_by_last_id():
        return storage.get_first_by_sniffed_data(Spi).clock_rate

    def insert(self):
        storage.insert(self.spi)
        storage.save()

    def delete(self):
        storage.delete(self.spi)
        storage.save()

    def update(self, id, significant_bit: str, clk_state: int, clk_phase: int, data_size: int):
        spi_protocol_record: Spi = self.get_by_id(id)
        if spi_protocol_record:
            spi_protocol_record.significant_bit = significant_bit
            spi_protocol_record.clk_state = clk_state
            spi_protocol_record.clk_phase = clk_phase
            spi_protocol_record.data_size = data_size

        storage.save()
