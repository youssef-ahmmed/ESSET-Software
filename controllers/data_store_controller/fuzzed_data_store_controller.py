from ML.fuzzed_data_collector import FuzzedDataCollector
from models.dao.fuzzed_data_dao import FuzzedDataDao
from models.dto.fuzzed_data_dto import FuzzedDataDto


class FuzzedDataStoreController:
    def __init__(self):
        super().__init__()
        self.fuzzed_data_dto = None
        self.fuzzed_data_dao = None

    def store_fuzzed_data(self):
        FuzzedDataDao.delete_all()
        message_response_data = FuzzedDataCollector().construct_message_response_table()
        for message_response_dict in message_response_data:
            self.fuzzed_data_dto = FuzzedDataDto(**message_response_dict)
            self.fuzzed_data_dao = FuzzedDataDao(self.fuzzed_data_dto)
            self.fuzzed_data_dao.insert()
