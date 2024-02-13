from PyQt5.QtCore import QObject

from controllers.display_controller.abstract_classes.data_display_collector_controller import \
    DataDisplayCollectorController
from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.n_bit_sniffing_dao import NBitSniffingDao
from models.dao.one_bit_sniffing_dao import OneBitDao
from models.dao.spi_protocol_dao import SpiProtocolDao
from models.dao.uart_protocol_dao import UartProtocolDao


class DataDisplayStartTimeController(DataDisplayCollectorController, QObject):

    def __init__(self):
        super().__init__()
        self.sniffing_option = SearchTimestampController.get_instance().get_sniffing_option()

        self.start_time = SearchTimestampController.get_instance().get_start_time_obj()
        self.channels_data_by_start_time = ChannelsDataDao.get_data_by_start_time(self.start_time)

    def get_channels_data_by_start_time(self):
        terminal_data = self._get_channels_data(self.channels_data_by_start_time)
        return terminal_data

    def get_plot_data_by_start_time(self):
        return self._get_plot_data(self.channels_data_by_start_time)

    def get_waveform_frequency_by_start_time(self):
        dao_methods = {
            "UART": UartProtocolDao.get_baudrate_by_start_time,
            "SPI": SpiProtocolDao.get_clock_rate_by_start_time,
            "1Bit": OneBitDao.get_clock_rate_by_start_time,
            "NBit": NBitSniffingDao.get_clock_rate_by_start_time
        }
        return dao_methods.get(self.sniffing_option)(self.start_time)

    def get_start_time_data(self):
        time_period = 1 / (self.get_waveform_frequency_by_start_time())
        plot_data = self.get_plot_data_by_start_time()

        return time_period, plot_data
