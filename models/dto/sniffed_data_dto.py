from datetime import datetime


class SniffedDataDto:
    def __init__(self, start_time: datetime, time_taken: int, connection_way: str, communication_protocol_name: str):
        self.start_time = start_time
        self.time_taken = time_taken
        self.connection_way = connection_way
        self.communication_protocol_name = communication_protocol_name
