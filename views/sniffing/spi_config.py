from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, \
    QPushButton, QVBoxLayout, QFormLayout, QWidget, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from views.sniffing.channel_pins_dialog import ChannelPinsDialog


class SpiConfigurations(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Spi Settings")
        self.setGeometry(100, 100, 400, 300)

        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = (screen_geometry.height() - self.height()) / 2
        self.move(x, y)

        self.spi_settings()
        self.create_layout()

    def spi_settings(self):
        self.settings_widget = QWidget()
        self.base_layout = QFormLayout(self.settings_widget)

        row_spacing = 15
        self.base_layout.setVerticalSpacing(row_spacing)

        self.mosi_label = QLabel("MOSI")
        self.mosi_combo = QComboBox()

        self.mosi_combo.addItem("Select Channel")
        self.mosi_combo.addItems(["ch1", "ch2", "ch3", "ch4"])
        self.mosi_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.mosi_combo.setCurrentIndex(0)

        self.miso_label = QLabel("MISO")
        self.miso_combo = QComboBox()

        self.miso_combo.addItem("Select Channel")
        self.miso_combo.addItems(["ch1", "ch2", "ch3", "ch4"])
        self.miso_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.miso_combo.setCurrentIndex(0)

        self.clock_label = QLabel("Clock")
        self.clock_combo = QComboBox()

        self.clock_combo.addItem("Select Channel")
        self.clock_combo.addItems(["ch1", "ch2", "ch3", "ch4"])
        self.clock_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.clock_combo.setCurrentIndex(0)

        self.enable_label = QLabel("Enable")
        self.enable_combo = QComboBox()

        self.enable_combo.addItem("Select Channel")
        self.enable_combo.addItems(["ch1", "ch2", "ch3", "ch4"])
        self.enable_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.enable_combo.setCurrentIndex(0)

        self.significant_bit_label = QLabel("Significant Bit")
        self.significant_bit_combo = QComboBox()
        self.significant_bit_combo.addItems(["L", "M"])

        default_significant_bit = 'L'
        self.significant_bit_combo.setCurrentText(default_significant_bit)

        self.bits_per_transfer_label = QLabel("Bits Per Transfer")
        self.bits_per_transfer_combo = QComboBox()
        self.bits_per_transfer_combo.addItems(["8", "7", "6", "5"])

        default_bits_per_transfer = '8'
        self.bits_per_transfer_combo.setCurrentText(default_bits_per_transfer)

        self.clock_state_label = QLabel("Clock State")
        self.clock_state_combo = QComboBox()
        self.clock_state_combo.addItems(["0", "1"])

        default_clock_state = '0'
        self.clock_state_combo.setCurrentText(default_clock_state)

        self.clock_phase_label = QLabel("Clock Phase")
        self.clock_phase_combo = QComboBox()
        self.clock_phase_combo.addItems(["0", "1"])

        default_clock_phase = '0'
        self.clock_phase_combo.setCurrentText(default_clock_phase)

        self.base_layout.addRow(self.mosi_label, self.mosi_combo)
        self.base_layout.addRow(self.miso_label, self.miso_combo)
        self.base_layout.addRow(self.clock_label, self.clock_combo)
        self.base_layout.addRow(self.enable_label, self.enable_combo)
        self.base_layout.addRow(self.significant_bit_label, self.significant_bit_combo)
        self.base_layout.addRow(self.bits_per_transfer_label, self.bits_per_transfer_combo)
        self.base_layout.addRow(self.clock_state_label, self.clock_state_combo)
        self.base_layout.addRow(self.clock_phase_label, self.clock_phase_combo)

    def create_layout(self):
        layout = QVBoxLayout()

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_settings)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_settings)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)

        layout.addWidget(self.settings_widget)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_selected_channels(self):
        mosi = self.mosi_combo.currentText()
        miso = self.miso_combo.currentText()
        clock = self.clock_combo.currentText()
        enable = self.enable_combo.currentText()

        return mosi, miso, clock, enable

    def reset_settings(self):
        self.mosi_combo.setCurrentIndex(0)
        self.miso_combo.setCurrentIndex(0)
        self.clock_combo.setCurrentIndex(0)
        self.enable_combo.setCurrentIndex(0)
        self.significant_bit_combo.setCurrentText('L')
        self.bits_per_transfer_combo.setCurrentText('8')
        self.clock_state_combo.setCurrentText('0')
        self.clock_phase_combo.setCurrentText('0')

    def cancel_settings(self):
        self.close()

    def save_settings(self):
        mosi, miso, clock, enable = self.get_selected_channels()
        ChannelPinsDialog.selected_spi_channels(mosi, miso, clock, enable, "SPI")
