from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from qfluentwidgets import ComboBox

ATTACK_OPERATIONS = ["Sniffing", "Replay Attack", "Stream Finder", "Fuzzing"]


class AttackOperationSelect(QWidget):
    attack_operation_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.attack_operation_label = QLabel("Attack Operation")
        self.attack_operation_combo = ComboBox()

        self.init_ui()
        self.start_communication()

    def start_communication(self):
        self.attack_operation_combo.currentIndexChanged.connect(
            self.attack_operation_select_changed
        )

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setLayout(QHBoxLayout())

        self.attack_operation_combo.addItems(ATTACK_OPERATIONS)

        self.layout().addWidget(self.attack_operation_label)
        self.layout().addWidget(self.attack_operation_combo)

    def get_selected_option(self):
        return self.attack_operation_combo.currentText()

    def attack_operation_select_changed(self, index):
        self.attack_operation_changed.emit(index)
