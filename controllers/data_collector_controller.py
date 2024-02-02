from PyQt5.QtCore import QObject

from controllers.sniffing_controller.dialogs_controller.bits_input_dialog_controller import BitsInputDialogController
from controllers.sniffing_controller.buttons_controller.channel_pins_button_controller import \
    ChannelPinsButtonController
from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.communication_protocol_controller.spi_dialog_controller import SpiDialogController
from controllers.sniffing_controller.communication_protocol_controller.uart_dialog_controller import \
    UartDialogController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController


class DataCollectorController(QObject):
    COMM_PROTOCOL = ['UART', 'SPI', 'I2C']
    CONNECTION_WAY = ['1Bit', 'NBits']

    def __init__(self):
        super().__init__()

    @staticmethod
    def collect_uart_data():
        uart_data = UartDialogController.get_instance().collect_uart_settings()
        uart_data.pop('top_level_name', None)
        uart_data.pop('option', None)
        uart_data.pop('channel_number', None)
        uart_data.pop('channel_name', None)
        uart_data['data_size'] = int(uart_data['data_size'])
        uart_data['stop_bit'] = int(uart_data['stop_bit'])
        return uart_data

    @staticmethod
    def collect_spi_data():
        spi_data = SpiDialogController.get_instance().collect_spi_settings()
        return {
            'significant_bit': spi_data['significant_bit'],
            'clk_state': int(spi_data['clk_state']),
            'clk_phase': int(spi_data['clk_phase']),
            'data_size': int(spi_data['data_size']),
        }

    @staticmethod
    def collect_one_bit_data():
        bits_data = BitsInputDialogController.get_instance().get_bits_number()
        option = bits_data.pop('option', None)
        if option == "NBits":
            return
        bits_data.pop('top_level_name', None)

        if option == "1Bit":
            bits_data["output_channel_number"] = bits_data.pop("channel_number")

        return bits_data

    @staticmethod
    def collect_n_bit_data():
        bits_data = BitsInputDialogController.get_instance().get_bits_number()
        option = bits_data.pop('option', None)
        if option == "1Bit":
            return
        bits_data.pop('top_level_name', None)
        if option == "NBits":
            return bits_data

    @staticmethod
    def collect_pin_planner_data():
        return ChannelPinsButtonController.get_instance().get_pin_planner_data()

    def collect_channels_data(self):
        communication_protocol = self.get_communication_protocol()
        connection_way = self.get_connection_way()
        if communication_protocol:
            return communication_protocol
        if connection_way:
            return connection_way

    def collect_sniffed_data(self):
        comm_protocol = CommProtocolSelectController.get_instance().get_selected_option()
        connection_way = NumberBitsSelectController.get_instance().get_selected_option()
        if comm_protocol not in self.COMM_PROTOCOL:
            comm_protocol = None
        if connection_way not in self.CONNECTION_WAY:
            connection_way = None
        sniffed_data = {
            'connection_way': connection_way,
            'communication_protocol_name': comm_protocol
        }
        return sniffed_data

    def get_communication_protocol(self):
        sniffed_data = self.collect_sniffed_data()
        selected_protocol = sniffed_data['communication_protocol_name']
        if selected_protocol == 'Select Comm Protocol' or selected_protocol == 'None':
            return
        elif selected_protocol == "UART":
            uart_data = UartDialogController.get_instance().collect_uart_settings()
            return {
                uart_data['channel_name']: int(uart_data['channel_name'][-1])
            }
        elif selected_protocol == "SPI":
            spi_data = SpiDialogController.get_instance().collect_spi_settings()
            return {
                'MOSI': int(spi_data['MOSI'][-1]),
                'MISO': int(spi_data['MISO'][-1]),
                'Clock': int(spi_data['Clock'][-1]),
                'Enable': int(spi_data['Enable'][-1])
            }

    def get_connection_way(self):
        sniffed_data = self.collect_sniffed_data()
        selected_connection_way = sniffed_data['connection_way']
        if selected_connection_way == 'None' or selected_connection_way == 'Select bits number':
            return
        elif selected_connection_way == '1Bit':
            one_bit_data = self.collect_one_bit_data()
            return {
                one_bit_data['channel_number']: 1
            }
        elif selected_connection_way == 'NBits':
            n_bit_data = self.collect_n_bit_data()
            return {
                n_bit_data['channel_number']: 1
            }
