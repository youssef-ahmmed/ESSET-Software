from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from qfluentwidgets import TableWidget


class ResponseTable(QWidget):
    def __init__(self):
        super().__init__()

        self.response_table = TableWidget()
        self.init_ui()

    def init_ui(self):
        self.response_table.setColumnCount(2)
        self.response_table.setRowCount(1000)
        self.response_table.setHorizontalHeaderLabels(["Message", "Response"])

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

    def table_resize_event(self, event):
        available_width = event.size().width()
        column0_width = int(available_width * 0.5)
        column1_width = int(available_width * 0.5)

        self.response_table.setColumnWidth(0, column0_width)
        self.response_table.setColumnWidth(1, column1_width)