import platform

from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from core.qsf_writer import QSFWriter
from core.vhdl_generator import VhdlGenerator

CLOCK_FREQUENCY = 50000000


class UartDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(uart_setting_dialog=None):
        if UartDialogController._instance is None:
            UartDialogController._instance = UartDialogController(uart_setting_dialog)
        return UartDialogController._instance

    def __init__(self, uart_setting_dialog):
        super(UartDialogController, self).__init__()

        if UartDialogController._instance is not None:
            raise Exception("An instance of SpiDialogController already exists. Use get_instance() to access it.")

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
            self.project_path_controller.show_error_dialog(self.uart_setting_dialog.save_button)
            return

        self.uart_configurations = self.collect_uart_settings()
        if self.uart_configurations is not None:
            self.uart_setting_dialog.accept()
            self.render_uart_templates()

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
            'clocks_per_bit':  int(CLOCK_FREQUENCY / bit_rate),
            'bits_per_frame': bits_per_frame,
            'channels_number': 8,
            'stop_bits': stop_bits,
            'parity_bit': parity_bit,
            'significant_bit': significant_bit
        }
        return uart_configurations

    def render_uart_templates(self):
        vhdl_generator = VhdlGenerator()
        qsf_writer = QSFWriter()

        template_names = [
            'top_level.vhd.jinja',
            'UART_Receiver.vhd.jinja',
            'UART_Transmitter.vhd.jinja',
            'Common_Ports.vhd.jinja',
            'Communication_Module.vhd.jinja'
        ]

        for template in template_names:
            vhdl_generator.render_template(template_name=template,
                                           configurations=self.uart_configurations, output_path=self.project_path)

        synthesis_template = 'synthesis_linux.sh.jinja' if platform.system() == 'Linux' else 'synthesis_windows.bat.jinja'
        vhdl_generator.render_template(template_name=synthesis_template,
                                       configurations=self.uart_configurations, output_path=self.project_path)
        qsf_writer.write_vhdl_files_to_qsf()
