from PyQt5.QtWidgets import QWidget, QHBoxLayout


class BaseModeWidget(QWidget):

    def __init__(self, widget):
        super().__init__()

        self.widget = widget

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())

        self.layout().addWidget(self.widget)
