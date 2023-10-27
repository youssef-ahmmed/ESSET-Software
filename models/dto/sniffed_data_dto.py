class SniffedDataDTO:
    def __init__(self, start_time, time_taken, data, connection_way, communication_protocol_name):
        self.start_time = start_time
        self.time_taken = time_taken
        self.data = data
        self.connection_way = connection_way
        self.communication_protocol_name = communication_protocol_name
