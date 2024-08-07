from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QCompleter
from qfluentwidgets import EditableComboBox


class SearchTimestamp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.search_label = QLabel("Search for data:")
        self.time_stamp_combobox = EditableComboBox()
        layout = QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.time_stamp_combobox)

        self.setLayout(layout)
        
    def update_timestamp_items(self, items):
        self.time_stamp_combobox.clear()
        self.time_stamp_combobox.addItems(["Choose Time Stamp"])
        self.time_stamp_combobox.addItems(items)
        self.time_stamp_combobox.setCurrentIndex(0)

        completer = QCompleter(items, self)
        self.time_stamp_combobox.setCompleter(completer)

    def set_enabled(self, enabled):
        self.search_label.setEnabled(enabled)
        self.time_stamp_combobox.setEnabled(enabled)
