from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter


class BaseModeWidget(QWidget):

    def __init__(self, left_widget, right_widget):
        super().__init__()

        self.left_widget = left_widget
        self.right_widget = right_widget

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.left_widget)
        self.layout().addWidget(self.right_widget)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left_widget)
        splitter.addWidget(self.right_widget)

        total_size = self.left_widget.sizeHint().width() + self.right_widget.sizeHint().width()

        size_vhdl = 0.99 * total_size
        size_settings = 0.01 * total_size

        splitter.setSizes([int(size_vhdl), int(size_settings)])

        self.layout().addWidget(splitter)
