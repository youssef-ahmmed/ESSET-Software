from PyQt5.QtWidgets import QWidget, QVBoxLayout

from views.sniffing.vhdl_editor_buttons import VhdlEditorButtons
from views.sniffing.vhdl_widget import VhdlWidget


class SniffingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.vhdl_widget = VhdlWidget()
        self.vhdl_editor_buttons = VhdlEditorButtons()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.vhdl_widget)
        self.layout().addWidget(self.vhdl_editor_buttons)
