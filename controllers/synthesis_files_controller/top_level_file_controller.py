from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import dir_list, split_pathname, join_paths


class TopLevelFileController(QObject):

    _instance = None

    @staticmethod
    def get_instance():
        if TopLevelFileController._instance is None:
            TopLevelFileController._instance = TopLevelFileController()
        return TopLevelFileController._instance

    def __init__(self):
        super(TopLevelFileController, self).__init__()
        if TopLevelFileController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.project_path = ProjectPathController.get_instance().get_project_path()

    def get_top_level_file_path(self) -> str | None:
        top_level_file_name = self.get_top_level_name()
        if top_level_file_name:
            return join_paths(self.project_path, top_level_file_name + '.vhd')
        return None

    def get_top_level_name(self) -> str | None:
        for file_name in dir_list(self.project_path):
            if file_name.endswith('.qsf'):
                return split_pathname(file_name)
        return None
