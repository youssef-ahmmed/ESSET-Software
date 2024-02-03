from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QCompleter
from qfluentwidgets import EditableComboBox


class SearchTimestamp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Search")

        self.init_ui()

    def init_ui(self):
        search_label = QLabel("Search for data:")
        self.time_stamp_combobox = EditableComboBox()
        layout = QVBoxLayout()
        layout.addWidget(search_label)
        layout.addWidget(self.time_stamp_combobox)

        self.setLayout(layout)
        
    def update_timestamp_items(self, items):
        self.time_stamp_combobox.clear()
        self.time_stamp_combobox.addItems(["Choose Time Stamp"])
        self.time_stamp_combobox.addItems(items)
        self.time_stamp_combobox.setCurrentIndex(0)

        completer = QCompleter(items, self)
        self.time_stamp_combobox.setCompleter(completer)
