class ChannelPinsDTO:
    def __init__(self, sniffed_data_id, channel_name, direction, hardware_pin):
        self.sniffed_data_id = sniffed_data_id
        self.channel_name = channel_name
        self.direction = direction
        self.hardware_pin = hardware_pin
