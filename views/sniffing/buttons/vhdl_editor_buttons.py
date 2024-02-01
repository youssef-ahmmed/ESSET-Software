from PyQt5.QtWidgets import QWidget, QHBoxLayout
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PushButton


class VhdlEditorButtons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_button = PushButton(FIF.DOWNLOAD, 'Load')
        self.save_button = PushButton(FIF.SAVE, 'Save')
        self.save_as_button = PushButton(FIF.SAVE_AS, 'Save As')

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.load_button)
        self.layout().addWidget(self.save_button)
        self.layout().addWidget(self.save_as_button)
