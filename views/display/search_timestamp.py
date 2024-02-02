from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from qfluentwidgets import EditableComboBox


class SearchTimestamp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Search")

        self.init_ui()

    def init_ui(self):
        search_label = QLabel("Search for data:")

        time_stamp_options = ["Choose Time Stamp", "Option 1", "Option 2", "Option 3"]
        time_stamp_combobox = EditableComboBox()
        time_stamp_combobox.addItems(time_stamp_options)
        time_stamp_combobox.setCurrentIndex(0)

        layout = QVBoxLayout()
        layout.addWidget(search_label)
        layout.addWidget(time_stamp_combobox)

        self.setLayout(layout)
