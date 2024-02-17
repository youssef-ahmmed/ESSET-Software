from PyQt5.QtCore import QObject

from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.communication_protocol_controller.spi_dialog_controller import SpiDialogController
from controllers.sniffing_controller.communication_protocol_controller.uart_dialog_controller import \
    UartDialogController
from controllers.sniffing_controller.dialogs_controller.bits_input_dialog_controller import BitsInputDialogController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController


class DataCollectorController(QObject):
    COMM_PROTOCOL = ['UART', 'SPI', 'I2C']
    CONNECTION_WAY = ['1Bit', 'NBits']
    DEFAULT_CHANNEL_NUMBER = 1

    def __init__(self):
        super().__init__()

    @staticmethod
    def collect_uart_data():
        uart_data = UartDialogController.get_instance().collect_uart_settings()
        database_keys = ['clk_per_bit', 'baud_rate', 'data_size', 'stop_bit', 'parity_bit', 'significant_bit']
        return {key: uart_data[key] for key in database_keys}

    @staticmethod
    def collect_spi_data():
        spi_data = SpiDialogController.get_instance().collect_spi_settings()
        database_keys = ['clock_rate', 'significant_bit', 'clk_state', 'clk_phase', 'data_size']
        return {key: spi_data[key] for key in database_keys}

    @staticmethod
    def collect_bits_data():
        bits_data = BitsInputDialogController.get_instance().get_bits_configurations()
        if bits_data['option'] == "One_Bit":
            return {
                'output_channel_number': bits_data['channel_number'],
                'clock_rate': bits_data['clock_rate']
            }
        elif bits_data['option'] == "NBits":
            return {
                'channel_number': bits_data['channel_number'],
                'clock_rate': bits_data['clock_rate']
            }
        return

    @staticmethod
    def collect_pin_planner_data():
        return PinPlannerDialogController.get_instance().get_pin_planner_data()

    def collect_channels_data(self):
        return self.get_communication_protocol_channels() or self.get_connection_way_channels()

    def collect_sniffing_option(self):
        comm_protocol = CommProtocolSelectController.get_instance().get_selected_option()
        connection_way = NumberBitsSelectController.get_instance().get_selected_option()
        if comm_protocol not in self.COMM_PROTOCOL:
            comm_protocol = None
        if connection_way not in self.CONNECTION_WAY:
            connection_way = None
        return {
            'connection_way': connection_way,
            'communication_protocol_name': comm_protocol
        }

    def get_communication_protocol_channels(self):
        selected_protocol = self.collect_sniffing_option()['communication_protocol_name']
        if selected_protocol == 'Choose':
            return
        elif selected_protocol == "UART":
            uart_data = UartDialogController.get_instance().collect_uart_settings()
            return {
                uart_data['channel_name']: int(uart_data['channel_name'][-1])
            }
        elif selected_protocol == "SPI":
            spi_data = SpiDialogController.get_instance().collect_spi_settings()
            return {
                'MOSI': spi_data['MOSI'][-1],
                'MISO': spi_data['MISO'][-1],
                'Clock': spi_data['Clock'][-1],
                'Enable': spi_data['Enable'][-1]
            }

    def get_connection_way_channels(self):
        selected_connection_way = self.collect_sniffing_option()['connection_way']
        if selected_connection_way == 'Choose':
            return
        elif selected_connection_way == '1Bit':
            return {
                'Channel 1': self.DEFAULT_CHANNEL_NUMBER
            }
        elif selected_connection_way == 'NBits':
            channel_number = self.collect_bits_data().get('channel_number') + 1
            return {
                f'Channel {num}': num for num in range(1, channel_number)
            }
