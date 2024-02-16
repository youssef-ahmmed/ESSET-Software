from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from qfluentwidgets import ComboBox


class NumberBitsSelect(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        bits_label = QLabel("Sniffing Bit Numbers")
        self.bits_combo = ComboBox()
        self.bits_combo.addItems(["Choose", "1Bit", "NBits"])

        self.layout().addWidget(bits_label)
        self.layout().addWidget(self.bits_combo)

    def get_selected_pin_number(self):
        return self.bits_combo.currentText()

    def reset_bits_selection(self):
        self.bits_combo.setCurrentText("Choose")
