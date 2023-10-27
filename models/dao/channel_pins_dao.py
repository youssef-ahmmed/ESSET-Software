from models.entities.channel_pins import ChannelPins
from models import storage


class ChannelPinsDAO:
    def __init__(self, channel_pins_dto):
        self.channel_pins_dto = channel_pins_dto
        self.channel_pins = ChannelPins()

        self.create_channel_pins()

    def create_channel_pins(self):
        self.channel_pins.channel_name = self.channel_pins_dto.channel_name
        self.channel_pins.hardware_pin = self.channel_pins_dto.hardware_pin
        self.channel_pins.direction = self.channel_pins_dto.direction

    def insert(self):
        storage.insert(self.channel_pins)
        storage.save()

    def delete(self):
        storage.delete(self.channel_pins)
        storage.save()

    def update(self, id, channel_name, hardware_pin, direction):
        channel_pins_record = storage.get_by_id(ChannelPins, id)
        if channel_pins_record:
            channel_pins_record.channel_name = channel_name
            channel_pins_record.hardware_pin = hardware_pin
            channel_pins_record.direction = direction

        storage.save()
