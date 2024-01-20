from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from controllers.sniffing_controller.buttons_controller.vhdl_editor_buttons_controller import \
    VhdlEditorButtonsController


class VhdlEditorButtons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_button = QPushButton('Load')
        self.save_button = QPushButton('Save')
        self.save_as_button = QPushButton('Save As')

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.load_button)
        self.layout().addWidget(self.save_button)
        self.layout().addWidget(self.save_as_button)
