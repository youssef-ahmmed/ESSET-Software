from datetime import datetime

from models.entities.sniffed_data import SniffedData
from models import storage
from models.dto.sniffed_data_dto import SniffedDataDto


class SniffedDataDao:
    def __init__(self, sniffed_data_dto: SniffedDataDto):
        self.sniffed_data_dto = sniffed_data_dto
        self.sniffed_data = SniffedData()

        self.create_sniffed_data()

    def create_sniffed_data(self):
        self.sniffed_data.start_time = self.sniffed_data_dto.start_time
        self.sniffed_data.time_taken = self.sniffed_data_dto.time_taken
        self.sniffed_data.connection_way = self.sniffed_data_dto.connection_way
        self.sniffed_data.communication_protocol_name = self.sniffed_data_dto.communication_protocol_name

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(SniffedData, id)

    @staticmethod
    def get_all():
        return storage.list_all(SniffedData)

    @staticmethod
    def get_last_sniffed_data_id():
        return storage.get_last_id(SniffedData)

    def insert(self):
        storage.insert(self.sniffed_data)
        storage.save()

    def delete(self):
        storage.delete(self.sniffed_data)
        storage.save()

    def update(self, id, start_time: datetime, time_taken: int, connection_way: str, communication_protocol_name: str):
        sniffed_data_record: SniffedData = self.get_by_id(id)
        if sniffed_data_record:
            sniffed_data_record.start_time = start_time
            sniffed_data_record.time_taken = time_taken
            sniffed_data_record.connection_way = connection_way
            sniffed_data_record.communication_protocol_name = communication_protocol_name

        storage.save()
