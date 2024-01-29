from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QComboBox, QPushButton, QHBoxLayout

from core.qsf_writer import QsfWriter


class HardwarePinPlanner(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pin_planner = QTableWidget()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        self.setWindowTitle("Hardware Pin Planner")
        self.init_ui()

        self.start_communication()

    def start_communication(self):
        self.save_button.clicked.connect(self.send_hardware_pins)
        self.cancel_button.clicked.connect(self.reject)

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.pin_planner.setMinimumSize(1000, 1000)
        self.pin_planner.setColumnCount(2)
        self.pin_planner.setHorizontalHeaderLabels(["Node Name", "Hardware Pin"])

        layout.addWidget(self.pin_planner)

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

    def populate_pin_planner(self, nodes_name):
        data = [
            (node, ["Pin 1", "Pin 2", "Pin 3"]) for node in nodes_name
        ]

        self.pin_planner.setRowCount(len(data))

        for row, (node_name, pin_list) in enumerate(data):
            self.pin_planner.setItem(row, 0, QTableWidgetItem(node_name))

            combobox = QComboBox()
            combobox.addItems(pin_list)
            self.pin_planner.setCellWidget(row, 1, combobox)

    def get_table_data(self) -> dict:
        table_data: dict[str, str] = {}

        for row in range(self.pin_planner.rowCount()):
            node_name = self.pin_planner.item(row, 0)
            hardware_pin = self.pin_planner.cellWidget(row, 1)

            if node_name is not None and hardware_pin is not None:
                node_name = node_name.text()
                hardware_pin = hardware_pin.currentText()
                table_data[node_name] = hardware_pin

        return table_data

    def send_hardware_pins(self):
        hardware_pins: dict[str, str] = self.get_table_data()

        qsf_writer = QsfWriter()
        qsf_writer.write_hardware_pins(hardware_pins)

        self.accept()
