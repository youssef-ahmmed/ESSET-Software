import platform

from PyQt5.QtCore import QObject
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from core.qsf_writer import QsfWriter
from core.vhdl_generator import VhdlGenerator
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.file_operations import delete_files
from views.common.info_bar import create_success_bar
from views.common.message_box import MessageBox

CLOCK_FREQUENCY = 50000000


class UartDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(parent=None, uart_setting_dialog=None):
        if UartDialogController._instance is None:
            UartDialogController._instance = UartDialogController(parent, uart_setting_dialog)
        return UartDialogController._instance

    def __init__(self, parent, uart_setting_dialog):
        super(UartDialogController, self).__init__()

        if UartDialogController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.parent = parent
        self.uart_setting_dialog = uart_setting_dialog
        self.project_path_controller = ProjectPathController.get_instance()

        self.handle_uart_settings_buttons()

    def handle_uart_settings_buttons(self):
        self.uart_setting_dialog.cancel_button.clicked.connect(self.uart_setting_dialog.reject)
        self.uart_setting_dialog.reset_button.clicked.connect(self.uart_setting_dialog.reset_settings)
        self.uart_setting_dialog.save_button.clicked.connect(self.save_uart_settings)

    def save_uart_settings(self):
        self.project_path = self.project_path_controller.get_project_path()

        if not self.project_path:
            MessageBox.show_project_path_error_dialog(self.uart_setting_dialog.save_button)
            return

        self.uart_configurations = self.collect_uart_settings()
        if self.uart_configurations is not None:
            self.uart_setting_dialog.accept()
            self.render_uart_templates()
            create_success_bar(self.parent, 'SUCCESS', log_messages.UART_CONFIG_SET)
            logger.success(log_messages.UART_CONFIG_SET)

    def show_uart_dialog(self):
        try:
            self.uart_setting_dialog.setParent(None)
            self.uart_setting_dialog.exec_()
        except Exception as e:
            print(f"Error in show_uart_dialog: {e}")

    def collect_uart_settings(self):
        input_channel = self.uart_setting_dialog.input_channel_combo.currentText()
        bit_rate = int(self.uart_setting_dialog.bitrate_combo.currentText())
        bits_per_frame = self.uart_setting_dialog.bits_per_frame_combo.currentText()
        stop_bits = self.uart_setting_dialog.stop_bits_combo.currentText()
        parity_bit = self.uart_setting_dialog.parity_combo.currentText()
        significant_bit = self.uart_setting_dialog.significant_bit_combo.currentText()

        if input_channel == "Select Channel":
            self.uart_setting_dialog.show_uart_channel_warning()
            return None

        uart_configurations = {
            'option': 'UART',
            'top_level_name': self.project_path_controller.get_top_level_name(),
            'clk_per_bit': int(CLOCK_FREQUENCY / bit_rate),
            'baud_rate': bit_rate,
            'data_size': bits_per_frame,
            'stop_bit': stop_bits,
            'parity_bit': parity_bit,
            'significant_bit': significant_bit,
            'channel_number': 8,
            'channel_name': input_channel
        }
        return uart_configurations

    def render_uart_templates(self):
        vhdl_generator = VhdlGenerator()
        qsf_writer = QsfWriter()

        template_names = [
            'top_level.vhd.jinja',
            'UART_Receiver.vhd.jinja',
            'UART_Transmitter.vhd.jinja',
            'Common_Ports.vhd.jinja',
            'Communication_Module.vhd.jinja'
        ]

        delete_files(self.project_path, '.vhd')

        for template in template_names:
            vhdl_generator.render_template(template_name=template,
                                           configurations=self.uart_configurations,
                                           output_path=self.project_path)

        synthesis_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux'else 'synthesis_windows.bat.jinja'
        vhdl_generator.render_template(template_name=synthesis_template,
                                       configurations=self.uart_configurations,
                                       output_path=self.project_path)
        qsf_writer.write_vhdl_files_to_qsf()
