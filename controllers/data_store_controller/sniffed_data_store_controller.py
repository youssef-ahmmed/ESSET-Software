from controllers.data_collector_controller import DataCollectorController
from models.dto.sniffed_data_dto import SniffedDataDto
from models.dao.sniffed_data_dao import SniffedDataDao
from datetime import datetime


class SniffedDataStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.sniffed_data_dto = None
        self.sniffed_data_dao = None

    def store_sniffed_data(self):
        self.sniffed_data_dto = SniffedDataDto(datetime.now(), 0,
                                               **self.data_collector_controller.get_sniffed_data())
        self.sniffed_data_dao = SniffedDataDao(self.sniffed_data_dto)
        self.sniffed_data_dao.insert()
