import os
import platform

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog
from loguru import logger

from models import log_messages
from reusable_functions.os_operations import split_pathname, join_paths, dir_list


class ProjectPathController(QObject):

    directory_path_changed = pyqtSignal(str)

    _instance = None

    @staticmethod
    def get_instance(parent=None):
        if ProjectPathController._instance is None:
            ProjectPathController._instance = ProjectPathController(parent)
        return ProjectPathController._instance

    def __init__(self, parent=None):
        super(ProjectPathController, self).__init__()
        if ProjectPathController._instance is not None:
            raise Exception("Controllers are singleton classes, please use the instance function")

        self.parent = parent
        self.project_path = ""
        self.env_path = ""

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
        qsf_files = [file for file in dir_list(self.project_path) if file.endswith('.qsf')]

        if qsf_files:
            return split_pathname(qsf_files[0])
        return "not exist"

    def get_qsf_file_path(self):
        qsf_file_path = [file for file in dir_list(self.project_path) if file.endswith('.qsf')]
        if not qsf_file_path:
            return "not exist"
        return join_paths(self.get_project_path(), ''.join(qsf_file_path))

    def get_script_path(self):
        script_extension = ".sh" if platform.system() == "Linux" else ".bat"
        script_files = [
            file for file in dir_list(self.project_path) if file.endswith(script_extension)
        ]

        if script_files:
            return join_paths(self.project_path, script_files[0])

        return None

    def get_sof_file(self) -> str | None:
        sof_dir_path = os.path.join(self.project_path, 'output_files')
        if not os.path.exists(sof_dir_path):
            return None
        sof_files = [file for file in os.listdir(sof_dir_path) if file.endswith('.sof')]
        if not sof_files:
            return None
        return os.path.join(sof_dir_path, sof_files[0])

    def open_env_path_dialog(self):
        env_path = QFileDialog.getExistingDirectory(None, 'Select Environment Path')
        if env_path:
            logger.success(log_messages.ENV_PATH_SET)
            self.env_path = env_path
        else:
            logger.warning(log_messages.NO_ENV_PATH)

    def get_env_path(self):
        return self.env_path
