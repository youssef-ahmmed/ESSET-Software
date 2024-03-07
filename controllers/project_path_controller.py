import platform

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog

from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import join_paths, dir_list
from views.common.info_bar import create_success_bar, create_warning_bar


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
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.project_path = ""

    def open_project_path_dialog(self):
        path = QFileDialog.getExistingDirectory(None, 'Select Project Directory')
        if path:
            self.project_path = path
            self.directory_path_changed.emit(self.project_path)
            create_success_bar(log_messages.QUARTUS_PATH_SPECIFIED)
        else:
            create_warning_bar(log_messages.NO_QUARTUS_PATH)

    def get_project_path(self):
        return self.project_path

    def is_project_path_exists(self) -> bool:
        return self.project_path != ""

    def get_script_path(self):
        script_extension = ".sh" if platform.system() == "Linux" else ".bat"
        for file_name in dir_list(self.project_path):
            if file_name.endswith(script_extension):
                return join_paths(self.project_path, file_name)
        return None
