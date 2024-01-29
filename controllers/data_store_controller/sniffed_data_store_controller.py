from datetime import datetime

from controllers.data_collector_controller import DataCollectorController
from models.dao.sniffed_data_dao import SniffedDataDao
from models.dto.sniffed_data_dto import SniffedDataDto


class SniffedDataStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.sniffed_data_dto = None
        self.sniffed_data_dao = None

    def store_sniffed_data(self, time_taken):
        self.sniffed_data_dto = SniffedDataDto(datetime.now(),
                                               time_taken,
                                               **self.data_collector_controller.collect_sniffed_data())
        self.sniffed_data_dao = SniffedDataDao(self.sniffed_data_dto)
        self.sniffed_data_dao.insert()
