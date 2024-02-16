from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout, QHBoxLayout, QCompleter
from qfluentwidgets import FluentIcon as FIF, StrongBodyLabel, EditableComboBox
from qfluentwidgets import TableWidget, PrimaryPushButton
from qframelesswindow import FramelessDialog

from models import log_messages


class HardwarePinPlanner(FramelessDialog):
    def __init__(self, info_bar=None):
        super().__init__()

        self.info_bar = info_bar
        self.pin_planner = TableWidget()
        self.save_button = PrimaryPushButton(FIF.SAVE, "Save")
        self.cancel_button = PrimaryPushButton(FIF.CANCEL_MEDIUM, "Cancel")
        self.reset_button = PrimaryPushButton(FIF.CANCEL_MEDIUM, "Reset")

        self.init_ui()
        self.create_layout()

    def init_ui(self):
        self.setContentsMargins(0, 20, 0, 0)

        self.title = StrongBodyLabel("Hardware Pin Planner")
        self.title.setAlignment(Qt.AlignCenter)

        self.pin_planner.setMinimumSize(500, 400)
        self.pin_planner.setColumnCount(2)
        self.pin_planner.setHorizontalHeaderLabels(["Node Name", "Hardware Pin"])

    def create_layout(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.title)
        layout.addWidget(self.pin_planner)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

    def populate_pin_planner(self, nodes_name):
        data = [(node, log_messages.PINS_NUMBERS) for node in nodes_name]

        self.pin_planner.setRowCount(len(data))

        for row, (node_name, pin_list) in enumerate(data):
            self.pin_planner.setItem(row, 0, QTableWidgetItem(node_name))

            combobox = EditableComboBox()
            combobox.addItems(pin_list)
            completer = QCompleter(pin_list, self)
            combobox.setCompleter(completer)
            self.pin_planner.setCellWidget(row, 1, combobox)
