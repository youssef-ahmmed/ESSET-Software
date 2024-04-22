from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import ProgressBar, InfoBadge


class MessageProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.progress_bar = ProgressBar()
        self.progress_bar.setFixedHeight(7)
        self.progress_bar.setValue(50)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.progress_bar)
        self.layout().addWidget(InfoBadge.success(800))
