import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtCore import Qt


class SearchTimestamp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Search")

        self.init_ui()

    def init_ui(self):

        self.search_label = QLabel("Search for data:")

        self.time_stamp_options = ["Choose Time Stamp", "Option 1", "Option 2", "Option 3"]
        self.time_stamp_combobox = QComboBox()
        self.time_stamp_combobox.addItems(self.time_stamp_options)
        self.time_stamp_combobox.setItemData(0, 0, role=Qt.UserRole - 1)
        self.time_stamp_combobox.setCurrentIndex(0)
        self.time_stamp_combobox.setEditable(True)

        layout = QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.time_stamp_combobox)

        self.setLayout(layout)
