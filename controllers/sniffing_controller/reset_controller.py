from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.communication_protocol_controller.spi_dialog_controller import SpiDialogController
from controllers.sniffing_controller.communication_protocol_controller.uart_dialog_controller import \
    UartDialogController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from controllers.sniffing_controller.number_bits_select_controller import NumberBitsSelectController
from controllers.sniffing_controller.terminal_controller import TerminalController


class ResetController:

    @staticmethod
    def clear_all_previous_configuration():
        comm_protocol_selected = CommProtocolSelectController.get_instance().get_selected_option()
        number_bit_selected = NumberBitsSelectController.get_instance()
        connection_way = number_bit_selected.get_selected_option()

        ResetController.comm_protocol_settings_reset(comm_protocol_selected)

        if connection_way != 'Choose':
            number_bit_selected.restart_settings()

        TerminalController.get_instance().clear_terminal()
        PinPlannerDialogController.get_instance().reset_pin_planner_table()

    @staticmethod
    def comm_protocol_settings_reset(comm_protocol_selected):
        if comm_protocol_selected == 'SPI':
            SpiDialogController.get_instance().restart_settings()
        elif comm_protocol_selected == 'UART':
            UartDialogController.get_instance().restart_settings()
