from controllers.data_collector_controller import DataCollectorController
from models.dao.sniffed_data_dao import SniffedDataDao
from models.dao.spi_protocol_dao import SpiProtocolDao
from models.dto.spi_protocol_dto import SpiProtocolDto


class SpiStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.spi_protocol_dto = None
        self.spi_protocol_dao = None

    def store_spi_protocol(self):
        spi_data = self.data_collector_controller.collect_spi_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        self.spi_protocol_dto = SpiProtocolDto(last_sniffed_data_id, **spi_data)
        self.spi_protocol_dao = SpiProtocolDao(self.spi_protocol_dto)
        self.spi_protocol_dao.insert()
