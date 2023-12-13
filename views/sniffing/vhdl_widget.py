from PyQt5.QtWidgets import QWidget, QVBoxLayout

from controller.project_path_controller import ProjectPathController
from controller.sniffing_controller.buttons_controller.vhdl_editor_buttons_controller import \
    VhdlEditorButtonsController
from views.sniffing.buttons.vhdl_editor_buttons import VhdlEditorButtons
from views.sniffing.vhdl_editor import VhdlEditor


class VhdlWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.vhdl_editor = VhdlEditor()
        self.vhdl_editor_buttons = VhdlEditorButtons()

        self.vhdl_editor_button_controller = VhdlEditorButtonsController(self.vhdl_editor.editor,
                                                                         self.vhdl_editor_buttons)
        self.project_path_controller = ProjectPathController.get_instance()

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(self.vhdl_editor)
        self.layout().addWidget(self.vhdl_editor_buttons)

    def start_communication(self):
        self.project_path_controller.directory_path_changed.connect(self.vhdl_editor.update_project_path_label)
        self.vhdl_editor.editor_tab_changed.connect(self.change_current_editor)
        self.vhdl_editor_button_controller.file_path_changed.connect(
            lambda file_path: self.vhdl_editor.change_editor_label(
                self.vhdl_editor.editor_index, file_path
            )
        )

    def change_current_editor(self, index):
        editor = self.vhdl_editor.editor_list[index]
        current_file_path = editor.current_file_path
        self.vhdl_editor_button_controller.set_new_editor_view(
            editor, current_file_path
        )
