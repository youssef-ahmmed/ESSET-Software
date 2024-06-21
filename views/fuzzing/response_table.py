from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import TableWidget, ToolButton


class ResponseTable(QWidget):
    def __init__(self):
        super().__init__()

        self.response_table = TableWidget()
        self.init_ui()

    def init_ui(self):
        self.response_table.setColumnCount(4)

        self.response_table.setHorizontalHeaderLabels(["Message", "Response", "Response Type", "Info"])

        layout = QVBoxLayout()
        layout.addWidget(self.response_table)
        self.setLayout(layout)
        self.response_table.resizeEvent = self.table_resize_event

    def create_table_rows(self, random_data: list):
        number_of_rows = len(random_data)

        current_row_count = self.response_table.rowCount()
        if number_of_rows > current_row_count:
            self.response_table.setRowCount(number_of_rows)
        elif number_of_rows < current_row_count:
            self.response_table.setRowCount(number_of_rows)

        for row in range(number_of_rows):
            message_text = random_data[row][0]
            response_text = random_data[row][1]
            response_type_text = random_data[row][2]

            if row < current_row_count:
                message_item = self.response_table.item(row, 0)
                response_item = self.response_table.item(row, 1)
                response_type_item = self.response_table.item(row, 2)
            else:
                message_item = QTableWidgetItem()
                response_item = QTableWidgetItem()
                response_type_item = QTableWidgetItem()

            message_item.setText(message_text)
            response_item.setText(response_text)
            response_type_item.setText(response_type_text)

            message_item.setFlags(message_item.flags() & ~Qt.ItemIsEditable)
            response_item.setFlags(response_item.flags() & ~Qt.ItemIsEditable)
            response_type_item.setFlags(response_type_item.flags() & ~Qt.ItemIsEditable)

            if row >= current_row_count:
                self.response_table.setItem(row, 0, message_item)
                self.response_table.setItem(row, 1, response_item)
                self.response_table.setItem(row, 2, response_type_item)

            self.response_table.setCellWidget(row, 3, ToolButton(FIF.MESSAGE, self.response_table))

    def delete_all_data(self):
        self.response_table.clearContents()
        self.response_table.setRowCount(0)

    def table_resize_event(self, event):
        available_width = event.size().width()
        column0_width = int(available_width * 0.3)
        column1_width = int(available_width * 0.3)
        column2_width = int(available_width * 0.3)
        column3_width = int(available_width * 0.1)

        self.response_table.setColumnWidth(0, column0_width)
        self.response_table.setColumnWidth(1, column1_width)
        self.response_table.setColumnWidth(2, column2_width)
        self.response_table.setColumnWidth(3, column3_width)
