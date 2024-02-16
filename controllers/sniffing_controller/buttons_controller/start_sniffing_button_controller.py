import platform

from PyQt5.QtCore import QObject
from qfluentwidgets import PrimarySplitPushButton

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.comm_protocol_select_controller import CommProtocolSelectController
from controllers.sniffing_controller.communication_protocol_controller.spi_dialog_controller import SpiDialogController
from controllers.sniffing_controller.communication_protocol_controller.uart_dialog_controller import \
    UartDialogController
from controllers.sniffing_controller.dialogs_controller.hardware_pin_planner_controller import \
    HardwarePinPlannerController
from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController
from core.command_executor import CommandExecutor
from core.script_executor import ScriptExecutor
from core.vhdl_generator import VhdlGenerator
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths
from views.common.info_bar import create_error_bar


class StartSniffingButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_sniffing_button: PrimarySplitPushButton = None) -> None:
        if StartSniffingButtonController._instance is None:
            StartSniffingButtonController._instance = StartSniffingButtonController(start_sniffing_button)
        return StartSniffingButtonController._instance

    def __init__(self, start_sniffing_button: PrimarySplitPushButton) -> None:
        super(StartSniffingButtonController, self).__init__()

        if StartSniffingButtonController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.start_sniffing_button = start_sniffing_button
        self.project_path_controller = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self) -> None:
        self.start_sniffing_button.clicked.connect(self.check_sof_file)

    def check_sof_file(self) -> None:
        sof_file_path = self.project_path_controller.get_sof_file_path()
        if not sof_file_path:
            create_error_bar(log_messages.NO_SOF_FILE)
            return

        try:
            self.generate_svf_file()
            SniffingTimerDialogController.get_instance().show_sniffing_timer_dialog()
        except Exception:
            create_error_bar(log_messages.NO_ENV_PATH)

    def generate_svf_file(self):
        top_level_path = join_paths(self.project_path_controller.get_project_path(), 'output_files',
                                    self.project_path_controller.get_top_level_name())
        input_sof_file = top_level_path + '.sof'
        output_svf_file = top_level_path + '.svf'
        quartus_cpf_command = f"quartus_cpf -c -q 25MHz -g 3.3 -n p {input_sof_file} {output_svf_file}"
        command_executor = CommandExecutor(quartus_cpf_command)
        command_executor.execute_command()

    @staticmethod
    def clear_all_previous_configuration():
        comm_protocol_selected = CommProtocolSelectController.get_instance().get_selected_option()
        number_bit_selected = NumberBitsSelectController.get_instance()
        connection_way = number_bit_selected.get_selected_option()

        StartSniffingButtonController.comm_protocol_settings_reset(comm_protocol_selected)

        if connection_way != 'Choose':
            number_bit_selected.restart_settings()

        TerminalController.get_instance().clear_terminal()
        HardwarePinPlannerController.get_instance().reset_table()

    @staticmethod
    def comm_protocol_settings_reset(comm_protocol_selected):
        if comm_protocol_selected == 'SPI':
            SpiDialogController.get_instance().restart_settings()
        elif comm_protocol_selected == 'UART':
            UartDialogController.get_instance().restart_settings()
