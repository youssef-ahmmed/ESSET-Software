from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QComboBox, QLabel, QHBoxLayout


class NumberBitsSelect(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.bits_label = QLabel("Sniffing Bit Numbers")
        self.bits_combo = QComboBox()
        self.bits_combo.addItem("Select bits number")
        self.bits_combo.addItems(["1Bit", "NBits", "None"])
        self.bits_combo.setItemData(0, 0, role=Qt.UserRole - 1)
        self.bits_combo.setCurrentIndex(0)

        layout.addWidget(self.bits_label)
        layout.addWidget(self.bits_combo)

        self.setLayout(layout)

    def get_selected_pin_number(self):
        return self.bits_combo.currentText()
