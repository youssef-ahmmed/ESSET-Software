from typing import Any

from models import storage
from models.dto.channels_data_dto import ChannelsDataDto
from models.entities.channels_data import ChannelsData


class ChannelsDataDao:
    def __init__(self, channels_data_dto: ChannelsDataDto):
        self.channels_data_dto = channels_data_dto
        self.channels_data = ChannelsData()

        self.create_channels_data()

    def create_channels_data(self):
        self.channels_data.sniffed_data_id = self.channels_data_dto.sniffed_data_id
        self.channels_data.channel_number = self.channels_data_dto.channel_number
        self.channels_data.channel_data = self.channels_data_dto.channel_data
        self.channels_data.channel_name = self.channels_data_dto.channel_name
        
    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(ChannelsData, id)

    @staticmethod
    def get_all():
        return storage.list_all(ChannelsData)

    def insert(self):
        storage.insert(self.channels_data)
        storage.save()

    def delete(self):
        storage.delete(self.channels_data)
        storage.save()
        
    def update(self, id, channel_number: int, channel_data: Any, channel_name: str):
        channel_data_record: ChannelsData = self.get_by_id(id)
        if channel_data_record:
            channel_data_record.channel_number = channel_number
            channel_data_record.channel_data = channel_data
            channel_data_record.channel_name = channel_name

        storage.save()
