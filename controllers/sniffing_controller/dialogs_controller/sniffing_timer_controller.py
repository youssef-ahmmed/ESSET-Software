from enum import IntEnum

from PyQt5.QtCore import QObject

from controllers.sniffing_controller.data_sniffing_collector_controller import DataCollectorController
from controllers.data_store_controller.channel_pins_store_controller import ChannelPinsStoreController
from controllers.data_store_controller.channels_data_store_controller import ChannelsDataStoreController
from controllers.data_store_controller.n_bit_store_controller import NBitStoreController
from controllers.data_store_controller.one_bit_store_controller import OneBitStoreController
from controllers.data_store_controller.sniffed_data_store_controller import SniffedDataStoreController
from controllers.data_store_controller.spi_store_controller import SpiStoreController
from controllers.data_store_controller.uart_store_controller import UartStoreController
from controllers.display_controller.search_timestamp_controller import SearchTimestampController
from controllers.project_path_controller import ProjectPathController
from core.ftp_sender import FtpSender
from models import log_messages
from models.log_messages import instance_exists_error
from views.common.info_bar import create_success_bar, create_warning_bar, create_error_bar
from views.sniffing.dialogs.sniffing_timer import SniffingTimer


class SniffingTimerDialogController(QObject):

    class TimeUnit(IntEnum):
        MINUTES = 60
        HOURS = 3600
        TWO_HOURS = 7200

    _instance = None

    @staticmethod
    def get_instance(parent=None, sniffing_timer_dialog: SniffingTimer = None):
        if SniffingTimerDialogController._instance is None:
            SniffingTimerDialogController._instance = SniffingTimerDialogController(parent, sniffing_timer_dialog)
        return SniffingTimerDialogController._instance

    def __init__(self, parent, sniffing_timer_dialog: SniffingTimer):
        super(SniffingTimerDialogController, self).__init__()

        if SniffingTimerDialogController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.sniffing_timer_dialog = sniffing_timer_dialog
        self.ok_button = self.sniffing_timer_dialog.ok_button
        self.cancel_button = self.sniffing_timer_dialog.cancel_button
        self.data_collector = DataCollectorController()
        self.parent = parent

        self.start_communication()

    def show_sniffing_timer_dialog(self):
        self.sniffing_timer_dialog.exec_()

    def start_communication(self):
        self.ok_button.clicked.connect(self.check_sniffing_config)
        self.cancel_button.clicked.connect(self.sniffing_timer_dialog.reject)

    def check_sniffing_config(self):
        try:
            connection_way, comm_protocol = self.data_collector.collect_sniffed_data().values()
            if not connection_way and not comm_protocol:
                create_error_bar(self.parent, "ERROR", log_messages.NO_CONFIGURATIONS_FOUND)
                return

            self.start_sniffing()
        except Exception:
            create_error_bar(self.parent, 'ERROR', log_messages.FTP_NOT_OPENED)

    def start_sniffing(self):
        self.store_sniffing_configurations()
        self.send_svf_file()

        create_success_bar(self.parent, 'SUCCESS', 'Sniffing Started Successfully ...')
        self.sniffing_timer_dialog.accept()

    def send_svf_file(self):
        project_path_controller = ProjectPathController.get_instance()
        svf_file_path = project_path_controller.get_svf_file_path()
        remote_file_path = f'Svf/top_level.svf'
        ftp_sender = FtpSender()
        ftp_sender.send_file_via_ftp(svf_file_path, remote_file_path)

    def store_sniffing_configurations(self):
        sniffed_data_store = SniffedDataStoreController()
        sniffed_data_store.store_sniffed_data(self.get_sniffing_time())

        channel_pins_store = ChannelPinsStoreController()
        channel_pins_store.store_channel_pins()

        connection_way, comm_protocol = self.data_collector.collect_sniffed_data().values()

        self.store_comm_protocol(comm_protocol)
        self.store_connection_way(connection_way)

        channels_data_store = ChannelsDataStoreController()
        channels_data_store.store_channels_data()

    def get_sniffing_time(self):
        sniffing_time = int(self.sniffing_timer_dialog.time_edit.text())
        time_unit = self.sniffing_timer_dialog.unit_combo.currentText()

        if time_unit == 'm':
            sniffing_time = sniffing_time * self.TimeUnit.MINUTES.value
        elif time_unit == 'h':
            sniffing_time = sniffing_time * self.TimeUnit.HOURS.value

        if sniffing_time >= self.TimeUnit.TWO_HOURS.value:
            create_warning_bar(self.parent, 'WARNING', log_messages.SNIFFING_TIME_WARNING)
            sniffing_time = self.TimeUnit.TWO_HOURS.value

        return sniffing_time

    @staticmethod
    def store_comm_protocol(comm_protocol):
        uart_store = UartStoreController()
        spi_store = SpiStoreController()
        comm_protocol_handlers = {
            'UART': uart_store.store_uart_protocol,
            'SPI': spi_store.store_spi_protocol,
        }
        if comm_protocol in comm_protocol_handlers:
            comm_protocol_handlers[comm_protocol]()

    @staticmethod
    def store_connection_way(connection_way):
        one_bit_store = OneBitStoreController()
        n_bit_store = NBitStoreController()
        connection_way_handlers = {
            '1Bit': one_bit_store.store_one_bit_sniffing,
            'NBits': n_bit_store.store_n_bit_sniffing,
        }
        if connection_way in connection_way_handlers:
            connection_way_handlers[connection_way]()
