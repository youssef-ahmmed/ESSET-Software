from controllers.data_collector_controller import DataCollectorController
from models.dto.channel_pins_dto import ChannelPinsDto
from models.dao.channel_pins_dao import ChannelPinsDao
from models.dao.sniffed_data_dao import SniffedDataDao


class ChannelPinsStoreController:
    def __init__(self):
        super().__init__()
        self.data_collector_controller = DataCollectorController()
        self.channel_pins_dto = None
        self.channel_pins_dao = None

    def store_channel_pins(self):
        channel_pins_data = self.data_collector_controller.collect_pin_planner_data()
        last_sniffed_data_id = SniffedDataDao.get_last_sniffed_data_id()

        for channel_name, hardware_pin in channel_pins_data.items():
            self.channel_pins_dto = ChannelPinsDto(last_sniffed_data_id, channel_name, hardware_pin)
            self.channel_pins_dao = ChannelPinsDao(self.channel_pins_dto)
            self.channel_pins_dao.insert()
