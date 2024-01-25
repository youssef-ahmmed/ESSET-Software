from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, \
    QPushButton, QVBoxLayout, QFormLayout, QWidget, QHBoxLayout, QApplication, QMessageBox
from loguru import logger

from models import log_messages


class SpiConfigurations(QDialog):
    def __init__(self):
        super().__init__()

        self.reset_button = None
        self.cancel_button = None
        self.save_button = None
        self.counter = 0
        self.initial_values = ["Select Channel", "ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8"]

        self.init_ui()
        self.set_up()

    def init_ui(self):
        self.setWindowTitle("Spi Settings")
        self.setGeometry(100, 100, 400, 300)

        screen_geometry = QApplication.desktop().availableGeometry()
        x = int((screen_geometry.width() - self.width()) / 2)
        y = int((screen_geometry.height() - self.height()) / 2)
        self.move(x, y)

    def set_up(self):
        self.spi_settings()
        self.create_layout()
        self.connect_signals()
        self.get_current_text()

    def spi_settings(self):
        self.settings_widget = QWidget()
        self.base_layout = QFormLayout(self.settings_widget)

        row_spacing = 15
        self.base_layout.setVerticalSpacing(row_spacing)

        mosi_label, self.mosi_combo = self.create_channels_combo_box("MOSI", QComboBox())
        miso_label, self.miso_combo = self.create_channels_combo_box("MISO", QComboBox())
        clock_label, self.clock_combo = self.create_channels_combo_box("Clock", QComboBox())
        enable_label, self.enable_combo = self.create_channels_combo_box("Enable", QComboBox())

        significant_bit_label, self.significant_bit_combo = self.create_setup_combo_box("Significant Bit",
                                                                                        ["L", "M"],
                                                                                        "L")
        bits_per_transfer_label, self.bits_per_transfer_combo = self.create_setup_combo_box("Bits Per Transfer",
                                                                                            ["8", "7", "6", "5"],
                                                                                            "8")
        clock_state_label, self.clock_state_combo = self.create_setup_combo_box("Clock State",
                                                                                ["0", "1"],
                                                                                "0")
        clock_phase_label, self.clock_phase_combo = self.create_setup_combo_box("Clock Phase",
                                                                                ["0", "1"],
                                                                                "0")

        self.base_layout.addRow(mosi_label, self.mosi_combo)
        self.base_layout.addRow(miso_label, self.miso_combo)
        self.base_layout.addRow(clock_label, self.clock_combo)
        self.base_layout.addRow(enable_label, self.enable_combo)
        self.base_layout.addRow(significant_bit_label, self.significant_bit_combo)
        self.base_layout.addRow(bits_per_transfer_label, self.bits_per_transfer_combo)
        self.base_layout.addRow(clock_state_label, self.clock_state_combo)
        self.base_layout.addRow(clock_phase_label, self.clock_phase_combo)

    def create_channels_combo_box(self, label_text, combo_box):
        label = QLabel(label_text)
        combo_box.addItems(self.initial_values)
        combo_box.setItemData(0, 0, role=Qt.UserRole - 1)
        combo_box.setCurrentIndex(0)
        return label, combo_box

    def create_setup_combo_box(self, label_text, items, default_value):
        label = QLabel(label_text)
        combo_box = QComboBox()
        combo_box.addItems(items)
        combo_box.setCurrentText(default_value)
        return label, combo_box

    def create_layout(self):
        layout = QVBoxLayout()

        self.reset_button = QPushButton("Reset")
        self.cancel_button = QPushButton("Cancel")
        self.save_button = QPushButton("Save")

        layout.addWidget(self.settings_widget)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_current_text(self):
        self.prev_b1 = self.mosi_combo.currentText()
        self.prev_b2 = self.miso_combo.currentText()
        self.prev_b3 = self.clock_combo.currentText()
        self.prev_b4 = self.enable_combo.currentText()

    def connect_signals(self):
        self.mosi_combo.currentIndexChanged.connect(self.update_comboboxes)
        self.miso_combo.currentIndexChanged.connect(self.update_comboboxes)
        self.clock_combo.currentIndexChanged.connect(self.update_comboboxes)
        self.enable_combo.currentIndexChanged.connect(self.update_comboboxes)

    def disconnect_signals(self):
        self.mosi_combo.currentIndexChanged.disconnect(self.update_comboboxes)
        self.miso_combo.currentIndexChanged.disconnect(self.update_comboboxes)
        self.clock_combo.currentIndexChanged.disconnect(self.update_comboboxes)
        self.enable_combo.currentIndexChanged.disconnect(self.update_comboboxes)

    def update_comboboxes(self):
        self.sender_combo_box = self.sender()
        self.selected_channel = self.sender_combo_box.currentText()

        self.current_texts = {combo_box: combo_box.currentText() for combo_box in
                              [self.mosi_combo, self.miso_combo, self.clock_combo, self.enable_combo]}

        self.pins_values = [self.mosi_combo, self.miso_combo, self.clock_combo, self.enable_combo]

        for combo_box in self.pins_values:
            combo_box.currentIndexChanged.disconnect(self.update_comboboxes)
            current_items = [combo_box.itemText(index) for index in range(combo_box.count())]
            combo_box.clear()
            items_without_selected = [item for item in current_items if item != self.selected_channel]
            combo_box.addItems(items_without_selected)

            if combo_box is self.sender_combo_box:
                self.update_sender_combobox(combo_box, items_without_selected)
            else:
                self.update_other_combobox(combo_box, items_without_selected)
            combo_box.currentIndexChanged.connect(self.update_comboboxes)

    def update_sender_combobox(self, combo_box, items_without_selected):
        if self.selected_channel != "Select Channel":
            if self.selected_channel not in items_without_selected:
                combo_box.addItem(self.selected_channel)

        combo_box.setCurrentText(self.selected_channel)
        self.combo_box_index = self.pins_values.index(combo_box) + 1
        self.prev_value = getattr(self, f"prev_b{self.combo_box_index}")

        self.update_prev_value(combo_box, items_without_selected)
        combo_box.model().sort(0)

    def update_prev_value(self, combo_box, items_without_selected):
        if self.prev_value != "Select Channel" and self.prev_value != self.selected_channel:
            if self.prev_value not in items_without_selected:
                combo_box.addItem(self.prev_value)
        combo_box.setCurrentText(self.selected_channel)

        for other_combo_box in self.pins_values:
            if other_combo_box is not self.sender_combo_box and self.selected_channel != "Select Channel":
                if self.prev_value not in [other_combo_box.itemText(index) for index in
                                           range(other_combo_box.count())]:
                    other_combo_box.addItem(self.prev_value)
                other_combo_box.setCurrentText(self.current_texts[other_combo_box])

        setattr(self, f"prev_b{self.combo_box_index}", self.selected_channel)

    def update_other_combobox(self, combo_box, items_without_selected):
        if self.prev_value != self.selected_channel and self.prev_value != "Select Channel":
            if self.prev_value not in items_without_selected:
                combo_box.addItem(self.prev_value)
        if (self.current_texts[combo_box] != "Select Channel" and self.current_texts[combo_box] not in
                items_without_selected):
            if self.current_texts[combo_box] not in items_without_selected:
                combo_box.addItem(self.current_texts[combo_box])
        combo_box.setCurrentText(self.current_texts[combo_box])
        combo_box.model().sort(0)

    def get_selected_channels(self):
        mosi = self.mosi_combo.currentText()
        miso = self.miso_combo.currentText()
        clock = self.clock_combo.currentText()
        enable = self.enable_combo.currentText()

        return mosi, miso, clock, enable

    def reset_settings(self):
        self.disconnect_signals()

        for combo_box in [self.mosi_combo, self.miso_combo, self.clock_combo, self.enable_combo]:
            combo_box.clear()
            combo_box.addItems(self.initial_values)
            combo_box.setCurrentIndex(0)

        self.connect_signals()

        self.significant_bit_combo.setCurrentText('L')
        self.bits_per_transfer_combo.setCurrentText('8')
        self.clock_state_combo.setCurrentText('0')
        self.clock_phase_combo.setCurrentText('0')
        logger.info(log_messages.SPI_RESET)

    @staticmethod
    def show_spi_channel_warning(channel_name):
        QMessageBox.warning(None, "Warning", f"No channel selected for {channel_name}")
