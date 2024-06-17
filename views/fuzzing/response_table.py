from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from qfluentwidgets import FluentIcon as FIF, MessageBox
from qfluentwidgets import TableWidget, ToolButton

from views.common.info_bar import main_window_manager


class ResponseTable(QWidget):
    def __init__(self):
        super().__init__()

        self.info_buttons = []
        self.response_table = TableWidget()
        self.init_ui()

    def init_ui(self):
        self.response_table.setColumnCount(3)

        self.response_table.setHorizontalHeaderLabels(["Message", "Response", "Info"])

        layout = QVBoxLayout()
        layout.addWidget(self.response_table)
        self.setLayout(layout)
        self.response_table.resizeEvent = self.table_resize_event

    def create_table_rows(self, random_data: list):
        number_of_rows = len(random_data)
        self.response_table.setRowCount(number_of_rows)

        for row in range(number_of_rows):
            if isinstance(random_data[row], list):
                message = QTableWidgetItem(''.join(map(str, random_data[row])))
            else:
                message = QTableWidgetItem(random_data[row])
            response = QTableWidgetItem("Response")

            message.setFlags(message.flags() & ~Qt.ItemIsEditable)
            response.setFlags(response.flags() & ~Qt.ItemIsEditable)

            self.response_table.setItem(row, 0, message)
            self.response_table.setItem(row, 1, response)
            info_button = ToolButton(FIF.MESSAGE, self.response_table)
            info_button.clicked.connect(lambda _, r=row: self.show_info_dialog(r))
            self.info_buttons.append(info_button)
            self.response_table.setCellWidget(row, 2, info_button)

    def show_info_dialog(self, row_number):
        message = self.response_table.item(row_number, 0).text()
        response = self.response_table.item(row_number, 1).text()

        title = f'Message Number [{row_number + 1}]'
        content = f"Message: {message}\n\nResponse: {response}"

        info_dialog = MessageBox(title, content, main_window_manager.main_window)
        info_dialog.cancelButton.hide()
        info_dialog.exec()

    def delete_all_data(self):
        self.response_table.clearContents()
        self.response_table.setRowCount(0)

    def table_resize_event(self, event):
        available_width = event.size().width()
        column0_width = int(available_width * 0.4)
        column1_width = int(available_width * 0.4)
        column2_width = int(available_width * 0.1)

        self.response_table.setColumnWidth(0, column0_width)
        self.response_table.setColumnWidth(1, column1_width)
        self.response_table.setColumnWidth(2, column2_width)
