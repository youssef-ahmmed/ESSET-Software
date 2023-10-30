from models.entities.one_bit_sniffing import OneBit
from models import storage


class OneBitDTO:
    def __init__(self, one_bit_dto):
        self.one_bit_dto = one_bit_dto
        self.one_bit = OneBit()

        self.create_one_bit()

    def create_one_bit(self):
        self.one_bit.sniffed_data_id = self.one_bit_dto.sniffed_data_id
        self.one_bit.output_channel_number = self.one_bit_dto.output_channel_number

    def get_by_id(self, id):
        return storage.get_by_id(OneBit, id)

    def get_all(self):
        return storage.list_all(OneBit)

    def insert(self):
        storage.insert(self.one_bit)
        storage.save()

    def delete(self):
        storage.delete(self.one_bit)
        storage.save()

    def update(self, id, output_channel_number):
        one_bit_record = self.get_by_id(id)
        if one_bit_record:
            one_bit_record.output_channel_number = output_channel_number

        storage.save()
