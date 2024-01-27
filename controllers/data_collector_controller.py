from PyQt5.QtCore import QObject

from controllers.sniffing_controller.bits_input_dialog_controller import BitsInputDialogController
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
        uart_data['bits_per_frame'] = int(uart_data['bits_per_frame'])
        uart_data['stop_bits'] = int(uart_data['stop_bits'])
        return uart_data

    @staticmethod
    def collect_spi_data():
        spi_data = SpiDialogController.get_instance().collect_spi_settings()
        spi_data.pop('top_level_name', None)
        spi_data['bits_per_transfer'] = int(spi_data['bits_per_transfer'])
        spi_data['clock_state'] = int(spi_data['clock_state'])
        spi_data['clock_phase'] = int(spi_data['clock_phase'])
        return spi_data

    @staticmethod
    def collect_one_bit_data():
        bits_data = BitsInputDialogController.get_instance().get_bits_number()
        option = bits_data.get('option', None)
        if option == "NBits":
            return
        bits_data.pop('top_level_name', None)

        if option == "1Bit":
            bits_data["output_channel_number"] = bits_data.pop("channel_number")

        return bits_data

    @staticmethod
    def collect_n_bit_data():
        bits_data = BitsInputDialogController.get_instance().get_bits_number()
        option = bits_data.get('option', None)
        if option == "1Bit":
            return
        bits_data.pop('top_level_name', None)
        if option == "NBits":
            return bits_data

    @staticmethod
    def collect_pin_planner_data():
        return ChannelPinsButtonController.get_instance().get_pin_planner_data()

    def get_sniffed_data(self):
        comm_protocol = CommProtocolSelectController.get_instance().get_selected_option()
        connection_way = NumberBitsSelectController.get_instance().get_selected_option()
        if comm_protocol not in self.COMM_PROTOCOL:
            comm_protocol = None
        if connection_way not in self.CONNECTION_WAY:
            connection_way = None
        sniffed_data = {
            'connection_way': connection_way,
            'comm_protocol': comm_protocol
        }
        return sniffed_data

    def get_communication_protocol(self):
        sniffed_data = self.get_sniffed_data()
        selected_protocol = sniffed_data['comm_protocol']
        if selected_protocol == 'Select Comm Protocol' or selected_protocol == 'None':
            return
        elif selected_protocol == "UART":
            uart_data = self.collect_uart_data()
            return {
                'option': uart_data['option'],
                'channel_name': uart_data['channel_name'],
                'channels_number': uart_data['channels_number']
            }
        elif selected_protocol == "SPI":
            spi_data = self.collect_spi_data()
            return {
                'option': spi_data['option'],
                'MOSI': spi_data['MOSI'],
                'MISO': spi_data['MISO'],
                'Clock': spi_data['Clock'],
                'Enable': spi_data['Enable']
            }

    def get_connection_way(self):
        sniffed_data = self.get_sniffed_data()
        selected_connection_way = sniffed_data['connection_way']
        if selected_connection_way == 'None' or selected_connection_way == 'Select bits number':
            return
        elif selected_connection_way == '1Bit':
            one_bit_data = self.collect_one_bit_data()
            return {
                'option': one_bit_data['option'],
                'channel_number': one_bit_data['channel_number'],
                'channel_name': 'CHANNEL_NAME'
            }
        elif selected_connection_way == 'NBits':
            n_bit_data = self.collect_n_bit_data()
            return {
                'option': n_bit_data['option'],
                'channel_number': n_bit_data['channel_number'],
                'channel_name': 'CHANNEL_NAME'
            }
