from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import TableWidget, ToolButton


class ResponseTable(QWidget):
    def __init__(self):
        super().__init__()

        self.response_table = TableWidget()
        self.init_ui()

    def init_ui(self):
        self.response_table.setColumnCount(3)
        self.response_table.setRowCount(100)
        self.response_table.setHorizontalHeaderLabels(["Message", "Response", "Info"])

        layout = QVBoxLayout()
        layout.addWidget(self.response_table)
        self.setLayout(layout)
        self.response_table.resizeEvent = self.table_resize_event

        #TODO: to be deleted
        for row in range(100):
            item1 = QTableWidgetItem(f"Message {row + 1}")
            item2 = QTableWidgetItem(f"Response {row + 1}")
            self.response_table.setItem(row, 0, item1)
            self.response_table.setItem(row, 1, item2)
            self.response_table.setCellWidget(row, 2, ToolButton(FIF.MESSAGE, self.response_table))

    def table_resize_event(self, event):
        available_width = event.size().width()
        column0_width = int(available_width * 0.4)
        column1_width = int(available_width * 0.4)
        column2_width = int(available_width * 0.1)

        self.response_table.setColumnWidth(0, column0_width)
        self.response_table.setColumnWidth(1, column1_width)
        self.response_table.setColumnWidth(2, column2_width)
