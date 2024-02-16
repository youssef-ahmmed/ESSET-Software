from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, \
    QVBoxLayout, QFormLayout, QWidget, QHBoxLayout, QApplication, QMessageBox
from loguru import logger
from qfluentwidgets import ComboBox, PrimaryPushButton, StrongBodyLabel, EditableComboBox
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessDialog

from models import log_messages
from views.common.info_bar import create_info_bar
from views.sniffing.dialogs.channel_pins_dialog import ChannelPinsDialog


class UartConfigurations(FramelessDialog):

    def __init__(self, parent=None):
        super().__init__()

        self.reset_button = None
        self.cancel_button = None
        self.save_button = None
        self.parent = parent

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)

        screen_geometry = QApplication.desktop().availableGeometry()
        x = int((screen_geometry.width() - self.width()) / 2)
        y = int((screen_geometry.height() - self.height()) / 2)
        self.move(x, y)

        self.uart_settings()
        self.create_layout()

    def uart_settings(self):
        self.settings_widget = QWidget()
        self.base_layout = QFormLayout(self.settings_widget)
        title = StrongBodyLabel("UART Configurations")
        title.setAlignment(Qt.AlignCenter)

        row_spacing = 15
        self.base_layout.setVerticalSpacing(row_spacing)

        self.input_channel_label = QLabel("Input Channel")
        self.input_channel_combo = ComboBox()

        self.input_channel_combo.addItem("Select Channel")
        self.input_channel_combo.addItems(["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8"])
        self.input_channel_combo.setCurrentIndex(0)

        self.bit_rate_label = QLabel("Bit Rate(Bits/s)")
        self.bitrate_combo = EditableComboBox()
        self.bitrate_combo.addItems(['110', '300', '600', '1200', '2400', '4800', '9600', '14400',
                                     '19200', '38400', '57600', '115200', '128000', '256000'])

        default_bitrate = '9600'
        self.bitrate_combo.setCurrentText(default_bitrate)

        self.bits_per_frame_label = QLabel("Bits Per Frame")
        self.bits_per_frame_combo = ComboBox()
        self.bits_per_frame_combo.addItems(["8", "7", "6", "5"])

        default_bits_per_frame = '8'
        self.bits_per_frame_combo.setCurrentText(default_bits_per_frame)

        self.stop_bits_label = QLabel("Stop Bits")
        self.stop_bits_combo = ComboBox()
        self.stop_bits_combo.addItems(["1", "2"])

        default_stop_bits = '1'
        self.stop_bits_combo.setCurrentText(default_stop_bits)

        self.parity_bit_label = QLabel("Parity Bit")
        self.parity_combo = ComboBox()
        self.parity_combo.addItems(["N", "E", "O"])

        default_parity_bit = 'N'
        self.parity_combo.setCurrentText(default_parity_bit)

        self.significant_bit_label = QLabel("Significant Bit")
        self.significant_bit_combo = ComboBox()
        self.significant_bit_combo.addItems(["L", "M"])

        default_significant_bit = 'L'
        self.significant_bit_combo.setCurrentText(default_significant_bit)

        self.base_layout.addRow(title)
        self.base_layout.addRow(self.input_channel_label, self.input_channel_combo)
        self.base_layout.addRow(self.bit_rate_label, self.bitrate_combo)
        self.base_layout.addRow(self.bits_per_frame_label, self.bits_per_frame_combo)
        self.base_layout.addRow(self.stop_bits_label, self.stop_bits_combo)
        self.base_layout.addRow(self.parity_bit_label, self.parity_combo)
        self.base_layout.addRow(self.significant_bit_label, self.significant_bit_combo)

    def create_layout(self):
        layout = QVBoxLayout()

        self.reset_button = PrimaryPushButton(FIF.REMOVE, "Reset")
        self.cancel_button = PrimaryPushButton(FIF.CANCEL_MEDIUM, "Cancel")
        self.save_button = PrimaryPushButton(FIF.SAVE, "Save")

        layout.addWidget(self.settings_widget)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_selected_input_channel(self):
        return self.input_channel_combo.currentText()

    def reset_settings(self):
        self.input_channel_combo.setCurrentIndex(0)
        self.bitrate_combo.setCurrentText('9600')
        self.bits_per_frame_combo.setCurrentText('8')
        self.stop_bits_combo.setCurrentText('1')
        self.parity_combo.setCurrentText('N')
        self.significant_bit_combo.setCurrentText('L')
        logger.info(log_messages.UART_RESET)
        create_info_bar(self.parent, 'INFO', log_messages.UART_RESET)

    def save_settings(self):
        input_channel = self.get_selected_input_channel()
        ChannelPinsDialog.selected_uart_channel(input_channel, 'UART')
        self.close()

    @staticmethod
    def show_uart_channel_warning():
        QMessageBox.warning(None, "Warning", f"No channel selected for input channel")
