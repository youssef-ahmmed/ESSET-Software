from controllers.sniffing_controller.data_sniffing_collector_controller import DataCollectorController
from models.dto.n_bit_sniffing_dto import NBitDto
from models.dao.n_bit_sniffing_dao import NBitSniffingDao
from models.dao.sniffed_data_dao import SniffedDataDao


class NBitStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.n_bit_dto = None
        self.n_bit_dao = None

    def store_n_bit_sniffing(self):
        n_bit_data = self.data_collector_controller.collect_bits_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        self.n_bit_dto = NBitDto(last_sniffed_data_id, **n_bit_data)
        self.n_bit_dao = NBitSniffingDao(self.n_bit_dto)
        self.n_bit_dao.insert()
