from models.entities.one_bit_sniffing import OneBit
from models import storage


class OneBitDTO:
    def __init__(self, one_bit_dto):
        self.one_bit_dto = one_bit_dto
        self.one_bit = OneBit()

        self.create_one_bit()

    def create_one_bit(self):
        self.one_bit.output_channel_number = self.one_bit_dto.output_channel_number

    def insert(self):
        storage.insert(self.one_bit)
        storage.save()

    def delete(self):
        storage.delete(self.one_bit)
        storage.save()

    def update(self, id, output_channel_number):
        one_bit_record = storage.get_by_id(OneBit, id)
        if one_bit_record:
            one_bit_record.output_channel_number = output_channel_number

        storage.save()
