from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton

from controller.project_path_controller import ProjectPathController


class VhdlEditorButtonsController(QObject):

    file_path_changed = pyqtSignal(str)

    def __init__(self, editor, editor_buttons):
        super(VhdlEditorButtonsController, self).__init__()

        self.editor = editor
        self.editor_buttons = editor_buttons

        self.start_communication()

    def start_communication(self):
        self.editor_buttons.load_button.clicked.connect(self.load_file)
        self.editor_buttons.save_button.clicked.connect(self.save_file)
        self.editor_buttons.save_as_button.clicked.connect(self.save_as)

    def set_new_editor_view(self, editor, current_file_path):
        self.editor = editor
        self.editor.current_file_path = current_file_path

    def load_file(self):
        project_path = ProjectPathController.get_instance().get_project_path()
        if project_path == "":
            self.show_error_dialog()
            return

        file_path, _ = QFileDialog.getOpenFileName(
            self.editor_buttons, "Open File", project_path, "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.editor.setPlainText(file.read())
                    self.editor.current_file_path = file_path
                self.file_path_changed.emit(file_path)
            except Exception as e:
                QMessageBox.warning(
                    self.editor_buttons, "Error", f"Error loading file: {str(e)}"
                )

    def save_file(self):
        if ProjectPathController.get_instance().get_project_path() == "":
            self.show_error_dialog()
            return

        if self.editor.current_file_path:
            try:
                with open(self.editor.current_file_path, 'w') as file:
                    file.write(self.editor.toPlainText())
            except Exception as e:
                QMessageBox.warning(
                    self.editor_buttons, "Error", f"Error saving file: {str(e)}"
                )
        else:
            self.save_as()

    def save_as(self):
        project_path = ProjectPathController.get_instance().get_project_path()
        if project_path == "":
            self.show_error_dialog()
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self.editor_buttons, "Save File As", project_path, "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.editor.toPlainText())
                self.editor.current_file_path = file_path
                self.file_path_changed.emit(file_path)
            except Exception as e:
                QMessageBox.warning(
                    self.editor_buttons, "Error", f"Error saving file: {str(e)}"
                )

    def show_error_dialog(self):
        error_dialog = QMessageBox(self.editor_buttons)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle('Error')
        error_dialog.setText("There is No Quartus Path Specified\n\nDo You Want to specify one ?")

        ok_button = QPushButton('OK')
        cancel_button = QPushButton('Cancel')

        error_dialog.addButton(ok_button, QMessageBox.AcceptRole)
        error_dialog.addButton(cancel_button, QMessageBox.RejectRole)

        result = error_dialog.exec_()

        if result == QMessageBox.AcceptRole:
            ProjectPathController.get_instance().open_directory_dialog()
        elif result == QMessageBox.RejectRole:
            pass
