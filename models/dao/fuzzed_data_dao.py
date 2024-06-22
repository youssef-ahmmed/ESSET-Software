from models import storage
from models.dto.fuzzed_data_dto import FuzzedDataDto
from models.entities.fuzzed_data import FuzzedData


class FuzzedDataDao:
    def __init__(self, fuzzed_data_dto: FuzzedDataDto):
        self.fuzzed_data_dto = fuzzed_data_dto
        self.fuzzed_data = FuzzedData()

        self.create_fuzzed_data()

    def create_fuzzed_data(self):
        self.fuzzed_data.message = self.fuzzed_data_dto.message
        self.fuzzed_data.message_length = self.fuzzed_data_dto.message_length
        self.fuzzed_data.message_entropy = self.fuzzed_data_dto.message_entropy
        self.fuzzed_data.response = self.fuzzed_data_dto.response
        self.fuzzed_data.response_length = self.fuzzed_data_dto.response_length
        self.fuzzed_data.response_entropy = self.fuzzed_data_dto.response_entropy

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(FuzzedData, id)

    @staticmethod
    def get_all():
        return storage.list_all(FuzzedData)

    @staticmethod
    def delete_all():
        all_fuzzed_data = storage.list_all(FuzzedData)
        for fuzzed_data in all_fuzzed_data:
            storage.delete(fuzzed_data)

        storage.save()

    @staticmethod
    def get_all_by_last_id():
        return storage.get_all_by_sniffed_data(FuzzedData)

    @staticmethod
    def get_last_not_null_data():
        return storage.get_last_not_null_data(FuzzedData)

    def insert(self):
        storage.insert(self.fuzzed_data)
        storage.save()

    def delete(self):
        storage.delete(self.fuzzed_data)
        storage.save()

    def update(self, id, message: str, message_length: int, message_entropy: float, 
               response: str, response_length: int, response_entropy: float):
        fuzzed_data_record: FuzzedData = self.get_by_id(id)
        if fuzzed_data_record:
            fuzzed_data_record.message = message
            fuzzed_data_record.message_length = message_length
            fuzzed_data_record.message_entropy = message_entropy
            fuzzed_data_record.response = response
            fuzzed_data_record.response_length = response_length
            fuzzed_data_record.response_entropy = response_entropy

        storage.save()
