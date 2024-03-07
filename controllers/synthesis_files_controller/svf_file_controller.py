from PyQt5.QtCore import QObject

from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import dir_list, split_pathname, join_paths


class SvfFileController(QObject):

    _instance = None

    @staticmethod
    def get_instance():
        if SvfFileController._instance is None:
            SvfFileController._instance = SvfFileController()
        return SvfFileController._instance

    def __init__(self):
        super(SvfFileController, self).__init__()
        if SvfFileController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.project_path = ProjectPathController.get_instance().get_project_path()

    def get_svf_file_path(self) -> str | None:
        output_files_path = join_paths(self.project_path, 'output_files')
        for file_name in dir_list(output_files_path):
            if file_name.endswith('.svf'):
                return join_paths(output_files_path, file_name)
        return None

