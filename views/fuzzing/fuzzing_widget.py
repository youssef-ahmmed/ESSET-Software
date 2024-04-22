from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from views.fuzzing.data_preparation_widget import DataPreparationWidget
from views.fuzzing.message_response_widget import MessageResponseWidget


class FuzzingWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.data_preparation_widget = DataPreparationWidget()
        self.message_response_widget = MessageResponseWidget()
        self.create_layout()

    def create_layout(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.data_preparation_widget)
        self.layout().addWidget(self.message_response_widget)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.data_preparation_widget)
        splitter.addWidget(self.message_response_widget)

        total_size = self.data_preparation_widget.sizeHint().width() + self.message_response_widget.sizeHint().width()
        left_side = 0.5 * total_size
        right_side = 0.5 * total_size

        splitter.setSizes([int(left_side), int(right_side)])
        self.layout().addWidget(splitter)
