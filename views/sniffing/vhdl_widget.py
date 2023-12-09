from PyQt5.QtWidgets import QWidget, QVBoxLayout

from views.sniffing.vhdl_editor import VhdlEditor
from views.sniffing.vhdl_editor_buttons import VhdlEditorButtons


class VhdlWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.vhdl_editor = VhdlEditor()
        self.vhdl_editor_buttons = VhdlEditorButtons()

        self.init_ui()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.vhdl_editor)
        self.layout().addWidget(self.vhdl_editor_buttons)

    def emit_add_new_path(self, project_path):
        self.vhdl_editor.update_project_path_label(project_path)
