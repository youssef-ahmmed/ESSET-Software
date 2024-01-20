from models.entities.channel_pins import ChannelPins
from models import storage
from models.dto.channel_pins_dto import ChannelPinsDto


class ChannelPinsDoa:
    def __init__(self, channel_pins_dto: ChannelPinsDto):
        self.channel_pins_dto = channel_pins_dto
        self.channel_pins = ChannelPins()

        self.create_channel_pins()

    def create_channel_pins(self):
        self.channel_pins.sniffed_data_id = self.channel_pins_dto.sniffed_data_id
        self.channel_pins.channel_name = self.channel_pins_dto.channel_name
        self.channel_pins.hardware_pin = self.channel_pins_dto.hardware_pin
        self.channel_pins.direction = self.channel_pins_dto.direction

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(ChannelPins, id)

    @staticmethod
    def get_all():
        return storage.list_all(ChannelPins)

    def insert(self):
        storage.insert(self.channel_pins)
        storage.save()

    def delete(self):
        storage.delete(self.channel_pins)
        storage.save()

    def update(self, id, channel_name: str, hardware_pin: str, direction: str):
        channel_pins_record: ChannelPins = self.get_by_id(id)
        if channel_pins_record:
            channel_pins_record.channel_name = channel_name
            channel_pins_record.hardware_pin = hardware_pin
            channel_pins_record.direction = direction

        storage.save()
