from controllers.data_collector_controller import DataCollectorController
from models.dto.channels_data_dto import ChannelsDataDto
from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.sniffed_data_dao import SniffedDataDao


class ChannelsDataStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.channels_data_dto = None
        self.channels_data_dao = None

    def store_channels_data(self):
        channels_data = self.data_collector_controller.collect_channels_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        for channel_name, channel_number in channels_data.items():
            self.channels_data_dto = ChannelsDataDto(last_sniffed_data_id, channel_name, channel_number, None)
            self.channels_data_dao = ChannelsDataDao(self.channels_data_dto)
            self.channels_data_dao.insert()
