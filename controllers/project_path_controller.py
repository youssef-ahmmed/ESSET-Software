import os
import platform

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton
from loguru import logger

from models import log_messages


class ProjectPathController(QObject):

    directory_path_changed = pyqtSignal(str)

    _instance = None

    @staticmethod
    def get_instance():
        if ProjectPathController._instance is None:
            ProjectPathController._instance = ProjectPathController()
        return ProjectPathController._instance

    def __init__(self):
        super(ProjectPathController, self).__init__()
        if ProjectPathController._instance is not None:
            raise Exception("Controllers are singleton classes, please use the instance function")

        self.project_path = ""

    def open_directory_dialog(self):
        directory_path = QFileDialog.getExistingDirectory(None, 'Select Project Directory')
        if directory_path:
            self.project_path = directory_path
            self.directory_path_changed.emit(directory_path)
            logger.success(log_messages.QUARTUS_PATH_SPECIFIED)
        else:
            logger.warning(log_messages.NO_QUARTUS_PATH)

    def get_project_path(self):
        return self.project_path

    def get_top_level_name(self):
        qsf_files = [file for file in os.listdir(self.project_path) if file.endswith('.qsf')]

        if qsf_files:
            qsf_file = qsf_files[0]
            return os.path.splitext(qsf_file)[0]
        return "not exist"

    def get_qsf_file_path(self):
        qsf_file_path = [file for file in os.listdir(self.project_path) if file.endswith('.qsf')]
        if not qsf_file_path:
            return "not exist"
        return os.path.join(self.get_project_path(), ''.join(qsf_file_path))

    def get_script_path(self):
        script_extension = ".sh" if platform.system() == "Linux" else ".bat"
        script_files = [
            file for file in os.listdir(self.project_path) if file.endswith(script_extension)
        ]

        if script_files:
            return os.path.join(self.project_path, script_files[0])

        return None

    def get_sof_file(self) -> bool | None:
        sof_dir_path = os.path.join(self.project_path, 'output_files')
        if not os.path.exists(sof_dir_path):
            return
        sof_file = [file for file in os.listdir(sof_dir_path) if file.endswith('.sof')]

        return len(sof_file) > 0

    @staticmethod
    def show_error_dialog(parent):
        error_dialog = QMessageBox(parent)
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
            logger.warning(log_messages.NO_QUARTUS_PATH)
