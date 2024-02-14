from controllers.sniffing_controller.data_sniffing_collector_controller import DataCollectorController
from models.dto.one_bit_sniffing_dto import OneBitDto
from models.dao.one_bit_sniffing_dao import OneBitDao
from models.dao.sniffed_data_dao import SniffedDataDao


class OneBitStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.one_bit_dto = None
        self.one_bit_dao = None

    def store_one_bit_sniffing(self):
        one_bit_data = self.data_collector_controller.collect_one_bit_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        self.one_bit_dto = OneBitDto(last_sniffed_data_id, **one_bit_data)
        self.one_bit_dao = OneBitDao(self.one_bit_dto)
        self.one_bit_dao.insert()
