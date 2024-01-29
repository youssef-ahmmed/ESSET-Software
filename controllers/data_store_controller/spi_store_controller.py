from controllers.data_collector_controller import DataCollectorController
from models.dto.spi_protocol_dto import SpiProtocolDto
from models.dao.spi_protocol_dao import SpiProtocolDao
from models.dao.sniffed_data_dao import SniffedDataDao


class SpiStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.spi_protocol_dto = None
        self.spi_protocol_dao = None

    def store_spi_protocol(self):
        if self.data_collector_controller.get_communication_protocol().get('option') == 'SPI':
            spi_data = self.data_collector_controller.collect_spi_data()
            last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

            self.spi_protocol_dto = SpiProtocolDto(last_sniffed_data_id, **spi_data)
            self.spi_protocol_dao = SpiProtocolDao(self.spi_protocol_dto)
            self.spi_protocol_dao.insert()
