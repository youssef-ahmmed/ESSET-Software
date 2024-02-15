from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog

from controllers.project_path_controller import ProjectPathController
from reusable_functions.dialog_message_box import show_error_message
from reusable_functions.file_operations import read_text_file, write_to_text_file
from views.common.message_box import MessageBox


class VhdlEditorButtonsController(QObject):

    file_path_changed = pyqtSignal(str)

    def __init__(self, editor, editor_buttons):
        super(VhdlEditorButtonsController, self).__init__()

        self.editor = editor
        self.editor_buttons = editor_buttons
        self.project_path_controller = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self):
        self.editor_buttons.load_button.clicked.connect(self.load_file)
        self.editor_buttons.save_button.clicked.connect(self.save_file)
        self.editor_buttons.save_as_button.clicked.connect(self.save_as)

    def set_new_editor_view(self, editor, current_file_path):
        self.editor = editor
        self.editor.current_file_path = current_file_path

    def load_file(self):
        project_path = self.project_path_controller.get_project_path()
        if project_path == "":
            MessageBox.show_project_path_error_dialog(self.editor)
            return

        file_path, _ = QFileDialog.getOpenFileName(
            self.editor_buttons, "Open File", project_path, "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                file_content = read_text_file(file_path)
                self.editor.setPlainText(file_content)
                self.editor.current_file_path = file_path
                self.file_path_changed.emit(file_path)
            except Exception as e:
                show_error_message(self.editor_buttons, f"Error loading file: {str(e)}")

    def save_file(self):
        if self.project_path_controller.get_project_path() == "":
            MessageBox.show_project_path_error_dialog(self.editor)
            return

        if self.editor.current_file_path:
            try:
                write_to_text_file(self.editor.current_file_path, self.editor.toPlainText())
            except Exception as e:
                show_error_message(self.editor_buttons, f"Error saving file: {str(e)}")
        else:
            self.save_as()

    def save_as(self):
        project_path = self.project_path_controller.get_project_path()
        if project_path == "":
            MessageBox.show_project_path_error_dialog(self.editor)
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self.editor_buttons, "Save File As", project_path, "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                write_to_text_file(file_path, self.editor.toPlainText())
                self.editor.current_file_path = file_path
                self.file_path_changed.emit(file_path)
            except Exception as e:
                show_error_message(self.editor_buttons, f"Error saving file: {str(e)}")
