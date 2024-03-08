from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from qfluentwidgets import ComboBox


class NumberBitsSelect(QWidget):
    sniff_number_bits_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.bits_combo = ComboBox()

        self.init_ui()
        self.start_communication()

    def start_communication(self):
        self.bits_combo.currentIndexChanged.connect(self.number_bits_changed)

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        bits_label = QLabel("Sniffing Bit Numbers")

        self.bits_combo.addItems(["Choose", "1Bit", "NBits"])

        self.layout().addWidget(bits_label)
        self.layout().addWidget(self.bits_combo)

    def get_selected_pin_number(self):
        return self.bits_combo.currentText()

    def number_bits_changed(self, index):
        self.sniff_number_bits_changed.emit(index)

    def reset_bits_selection(self):
        self.bits_combo.setCurrentText("Choose")
