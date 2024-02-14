from PyQt5.QtCore import QObject

from controllers.display_controller.abstract_classes.data_display_collector_controller import \
    DataDisplayCollectorController
from models.dao.channels_data_dao import ChannelsDataDao
from models.dao.n_bit_sniffing_dao import NBitSniffingDao
from models.dao.one_bit_sniffing_dao import OneBitDao
from models.dao.sniffed_data_dao import SniffedDataDao
from models.dao.spi_protocol_dao import SpiProtocolDao
from models.dao.uart_protocol_dao import UartProtocolDao


class DataDisplayLastIdController(DataDisplayCollectorController, QObject):

    def __init__(self):
        super().__init__()

        self.channels_data_by_last_id = ChannelsDataDao.get_last_not_null_data()[:1]

    def get_last_channels_data(self):
        terminal_data = self._get_channels_data(self.channels_data_by_last_id)
        return terminal_data

    def get_plot_data_by_last_id(self):
        return self._get_plot_data(self.channels_data_by_last_id)

    def get_sniffing_option(self):
        sniffing_option = SniffedDataDao.get_by_id(self.channels_data_by_last_id[0].sniffed_data_id)
        if sniffing_option.connection_way:
            return sniffing_option.connection_way
        elif sniffing_option.communication_protocol_name:
            return sniffing_option.communication_protocol_name

    def get_waveform_frequency_by_last_id(self):
        dao_methods = {
            "UART": UartProtocolDao.get_baudrate_by_last_id,
            "SPI": SpiProtocolDao.get_clock_rate_by_last_id,
            "1Bit": OneBitDao.get_clock_rate_by_last_id,
            "NBit": NBitSniffingDao.get_clock_rate_by_last_id
        }
        return dao_methods.get(self.get_sniffing_option())()

    def get_last_id_data(self):
        time_period = 1 / (self.get_waveform_frequency_by_last_id())
        plot_data = self.get_plot_data_by_last_id()

        return time_period, plot_data
