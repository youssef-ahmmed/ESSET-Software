from PyQt5.QtCore import QObject

from controllers.intercept_controller.stream_finder_input_controller import StreamFinderInputController
from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.attack_operation_select_controller import AttackOperationSelectController
from controllers.sniffing_controller.dialogs_controller.pin_planner_dialog_controller import PinPlannerDialogController
from controllers.template_generator_controller.operation_generator_controller import OperationGeneratorController
from models import log_messages
from models.log_messages import instance_exists_error
from views.common.info_bar import create_success_bar
from views.common.message_box import MessageBox

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
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.uart_setting_dialog = uart_setting_dialog
        self.project_path_controller = ProjectPathController.get_instance()

        self.handle_uart_settings_buttons()

    def handle_uart_settings_buttons(self):
        self.uart_setting_dialog.cancel_button.clicked.connect(self.uart_setting_dialog.reject)
        self.uart_setting_dialog.reset_button.clicked.connect(self.uart_setting_dialog.reset_settings)
        self.uart_setting_dialog.save_button.clicked.connect(self.save_uart_settings)

    def save_uart_settings(self):
        if not self.project_path_controller.get_project_path():
            MessageBox.show_project_path_error_dialog(self.uart_setting_dialog.save_button)
            return

        if self.collect_uart_settings():
            self.uart_setting_dialog.accept()
            OperationGeneratorController().render_uart_templates(self.collect_uart_settings())
            PinPlannerDialogController.get_instance().send_data_to_pin_planner()
            create_success_bar(log_messages.UART_CONFIG_SET)

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
            'option': self.get_uart_option(),
            'data_stream': StreamFinderInputController.get_instance().get_input_stream(),
            'clk_per_bit': int(CLOCK_FREQUENCY / bit_rate),
            'baud_rate': int(bit_rate),
            'data_size': int(bits_per_frame),
            'stop_bit': int(stop_bits),
            'parity_bit': parity_bit,
            'significant_bit': significant_bit,
            'channel_number': 8,
            'channel_name': input_channel
        }
        return uart_configurations

    def get_uart_option(self):
        uart_options = {
            "Sniffing": "UART Receiver",
            "Replay Attack": "UART Transmitter"
        }
        return uart_options.get(AttackOperationSelectController
                                .get_instance().get_selected_attack_operation())

    def restart_settings(self):
        self.uart_setting_dialog.reset_settings()
