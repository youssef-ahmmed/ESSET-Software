from models.entities.n_bit_sniffing import NBit
from models import storage
from models.dto.n_bit_sniffing_dto import NBitDto


class NBitSniffingDao:
    def __init__(self, n_bit_dto: NBitDto):
        self.n_bit_dto = n_bit_dto
        self.nbit = NBit()

        self.create_n_bit_sniffing()

    def create_n_bit_sniffing(self):
        self.nbit.sniffed_data_id = self.n_bit_dto.sniffed_data_id
        self.nbit.channel_number = self.n_bit_dto.channel_number

    @staticmethod
    def get_by_id(id):
        return storage.get_by_id(NBit, id)

    @staticmethod
    def get_all():
        return storage.list_all(NBit)

    def insert(self):
        storage.insert(self.nbit)
        storage.save()

    def delete(self):
        storage.delete(self.nbit)
        storage.save()

    def update(self, id, channel_number: int):
        n_bit_record: NBit = self.get_by_id(id)
        if n_bit_record:
            n_bit_record.channel_number = channel_number

        storage.save()
