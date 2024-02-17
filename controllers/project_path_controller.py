import platform

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog

from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.file_operations import get_files_with_extension
from reusable_functions.os_operations import split_pathname, join_paths, dir_list, check_path_exists
from views.common.info_bar import create_success_bar, create_warning_bar


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
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.parent = parent
        self.project_path = ""
        self.env_path = ""

    def open_project_path_dialog(self):
        self.project_path = self.open_directory_dialog('Select Project Directory', log_messages.QUARTUS_PATH_SPECIFIED,
                                                       log_messages.NO_QUARTUS_PATH)
        self.directory_path_changed.emit(self.project_path)

    def get_project_path(self):
        return self.project_path

    def is_project_path_exists(self) -> bool:
        return self.project_path != ""

    def is_top_level_exists(self) -> bool:
        if self.is_project_path_exists() and self.get_top_level_name() != "not exist":
            return True

    def get_top_level_name(self):
        qsf_files = get_files_with_extension(self.project_path, '.qsf')
        return split_pathname(qsf_files) if qsf_files else "not exist"

    def get_top_level_file_path(self):
        return join_paths(self.project_path, self.get_top_level_name() + ".vhd")

    def get_qsf_file_path(self):
        qsf_file = get_files_with_extension(self.project_path, '.qsf')
        return join_paths(self.project_path, qsf_file) if qsf_file else "not exist"

    def get_script_path(self):
        script_extension = ".sh" if platform.system() == "Linux" else ".bat"
        script_files = get_files_with_extension(self.project_path, script_extension)
        return join_paths(self.project_path, script_files) if script_files else None

    def get_sof_file_path(self) -> str:
        return get_files_with_extension(join_paths(self.project_path, 'output_files'), '.sof')

    def get_svf_file_path(self) -> str:
        return get_files_with_extension(join_paths(self.project_path, 'output_files'), '.svf')

    def open_env_path_dialog(self):
        self.env_path = self.open_directory_dialog('Select Environment Path', log_messages.ENV_PATH_SET,
                                                   log_messages.NO_ENV_PATH)

    def get_env_path(self):
        return self.env_path

    @staticmethod
    def open_directory_dialog(title, success_msg, warning_msg):
        path = QFileDialog.getExistingDirectory(None, title)
        if path:
            create_success_bar(success_msg)
            return path
        else:
            create_warning_bar(warning_msg)
