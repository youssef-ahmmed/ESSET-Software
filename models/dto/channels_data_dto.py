from typing import Any


class ChannelsDataDto:
    def __init__(self, sniffed_data_id: int, channel_number: int, channel_data: Any, channel_name: str):
        self.sniffed_data_id = sniffed_data_id
        self.channel_number = channel_number
        self.channel_data = channel_data
        self.channel_name = channel_name
