from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout


class VhdlEditorButtons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._load_button = QPushButton('Load')
        self._save_button = QPushButton('Save')
        self._save_as_button = QPushButton('Save As')
        self._revert_button = QPushButton('Revert')

        self.init_ui()

    def init_ui(self):
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self._load_button)
        self.layout().addWidget(self._save_button)
        self.layout().addWidget(self._save_as_button)
        self.layout().addWidget(self._revert_button)
