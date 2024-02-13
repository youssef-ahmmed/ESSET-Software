from models.entities.one_bit_sniffing import OneBit
from models import storage
from models.dto.one_bit_sniffing_dto import OneBitDto
from models.entities.sniffed_data import SniffedData


class OneBitDao:
    def __init__(self, one_bit_dto: OneBitDto):
        self.one_bit_dto = one_bit_dto
        self.one_bit = OneBit()

        self.create_one_bit()

    def create_one_bit(self):
        self.one_bit.sniffed_data_id = self.one_bit_dto.sniffed_data_id
        self.one_bit.output_channel_number = self.one_bit_dto.output_channel_number
        self.one_bit.clock_rate = self.one_bit_dto.clock_rate

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(OneBit, id)

    @staticmethod
    def get_all():
        return storage.list_all(OneBit)

    @staticmethod
    def get_clock_rate_by_start_time(start_time):
        return storage.get_all_by_join(SniffedData, OneBit, start_time)[0].clock_rate

    @staticmethod
    def get_clock_rate_by_last_id():
        return storage.get_first_by_sniffed_data(OneBit).clock_rate

    def insert(self):
        storage.insert(self.one_bit)
        storage.save()

    def delete(self):
        storage.delete(self.one_bit)
        storage.save()

    def update(self, id, output_channel_number: int):
        one_bit_record: OneBit = self.get_by_id(id)
        if one_bit_record:
            one_bit_record.output_channel_number = output_channel_number

        storage.save()
