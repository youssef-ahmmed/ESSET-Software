from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QComboBox


class HardwarePinPlanner(QDialog):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()

        self.setWindowTitle("Hardware Pin Planner")
        self.init_ui()
        self.populate_table()

    def init_ui(self):
        self.table.setMinimumSize(340, 200)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Node Name", "Direction", "Hardware Pin"])

        layout = QVBoxLayout(self)
        layout.addWidget(self.table)

    def populate_table(self):
        # TODO: Node Name and Direction should be parsed from the vhdl files
        data = [
            ("Node 1", "Input", ["Pin 1", "Pin 2", "Pin 3"]),
            ("Node 2", "Output", ["Pin 1", "Pin 2", "Pin 3"]),
            ("Node 3", "Input", ["Pin 1", "Pin 2", "Pin 3"]),
            ("Node 4", "Output", ["Pin 1", "Pin 2", "Pin 3"]),
            ("Node 5", "Input", ["Pin 1", "Pin 2", "Pin 3"]),
        ]

        self.table.setRowCount(len(data))

        for row, (node_name, direction, pin_list) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(node_name))
            self.table.setItem(row, 1, QTableWidgetItem(direction))

            combobox = QComboBox()
            combobox.addItems(pin_list)
            self.table.setCellWidget(row, 2, combobox)
