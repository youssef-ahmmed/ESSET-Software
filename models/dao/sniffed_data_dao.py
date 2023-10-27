from models.entities.sniffed_data import SniffedData
from models import storage


class SniffedDataDAO:
    def __init__(self, sniffed_data_dto):
        self.sniffed_data_dto = sniffed_data_dto
        self.sniffed_data = SniffedData()

        self.create_sniffed_data()

    def create_sniffed_data(self):
        self.sniffed_data.start_time = self.sniffed_data_dto.start_time
        self.sniffed_data.time_taken = self.sniffed_data_dto.time_taken
        self.sniffed_data.data = self.sniffed_data_dto.data
        self.sniffed_data.connection_way = self.sniffed_data_dto.connection_way
        self.sniffed_data.communication_protocol_name = self.sniffed_data_dto.communication_protocol_name

    def insert(self):
        storage.insert(self.sniffed_data)
        storage.save()

    def delete(self):
        storage.delete(self.sniffed_data)
        storage.save()

    def update(self, id, start_time, time_taken, data, connection_way, communication_protocol_name):
        sniffed_data_record = storage.get_by_id(SniffedData, id)
        if sniffed_data_record:
            sniffed_data_record.start_time = start_time
            sniffed_data_record.time_taken = time_taken
            sniffed_data_record.data = data
            sniffed_data_record.connection_way = connection_way
            sniffed_data_record.communication_protocol_name = communication_protocol_name

        storage.save()
