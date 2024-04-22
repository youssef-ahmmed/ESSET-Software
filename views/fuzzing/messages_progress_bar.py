from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import ProgressBar


class MessageProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.progress_bar = ProgressBar()
        self.progress_bar.setValue(70)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.progress_bar)
