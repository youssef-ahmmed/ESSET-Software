class ChannelPinsDto:
    def __init__(self, sniffed_data_id: int, channel_name: str, direction: str, hardware_pin: str):
        self.sniffed_data_id = sniffed_data_id
        self.channel_name = channel_name
        self.direction = direction
        self.hardware_pin = hardware_pin
