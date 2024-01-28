class ChannelPinsDto:
    def __init__(self, sniffed_data_id: int, channel_name: str, hardware_pin: str):
        self.sniffed_data_id = sniffed_data_id
        self.channel_name = channel_name
        self.hardware_pin = hardware_pin
