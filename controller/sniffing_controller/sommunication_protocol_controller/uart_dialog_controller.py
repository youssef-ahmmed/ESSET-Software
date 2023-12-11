from PyQt5.QtCore import QObject


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
        self.uart_configurations = []

        self.handle_uart_settings_buttons()

    def handle_uart_settings_buttons(self):
        self.uart_setting_dialog.cancel_button.clicked.connect(self.uart_setting_dialog.reject)
        self.uart_setting_dialog.reset_button.clicked.connect(self.uart_setting_dialog.reset_settings)
        self.uart_setting_dialog.save_button.clicked.connect(self.save_uart_settings)

    def save_uart_settings(self):
        self.uart_configurations = self.collect_uart_settings()
        if self.uart_configurations is not None:
            self.uart_setting_dialog.accept()

    def show_uart_dialog(self):
        try:
            self.uart_setting_dialog.setParent(None)
            self.uart_setting_dialog.exec_()
        except Exception as e:
            print(f"Error in show_uart_dialog: {e}")

    def collect_uart_settings(self):
        input_channel = self.uart_setting_dialog.input_channel_combo.currentText()
        bit_rate = self.uart_setting_dialog.bitrate_combo.currentText()
        bits_per_frame = self.uart_setting_dialog.bits_per_frame_combo.currentText()
        stop_bits = self.uart_setting_dialog.stop_bits_combo.currentText()
        parity_bit = self.uart_setting_dialog.parity_combo.currentText()
        significant_bit = self.uart_setting_dialog.significant_bit_combo.currentText()

        if input_channel == "Select Channel":
            self.uart_setting_dialog.show_uart_channel_warning()
            return None

        return [input_channel, bit_rate, bits_per_frame, stop_bits, parity_bit, significant_bit]
