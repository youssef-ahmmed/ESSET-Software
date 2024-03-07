from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from models import log_messages
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import dir_list, join_paths
from views.common.info_bar import create_error_bar


class SofFileController(QObject):

    _instance = None

    @staticmethod
    def get_instance():
        if SofFileController._instance is None:
            SofFileController._instance = SofFileController()
        return SofFileController._instance

    def __init__(self):
        super(SofFileController, self).__init__()
        if SofFileController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.project_path_instance = ProjectPathController.get_instance()

    def get_sof_file_path(self) -> str | None:
        output_files_path = join_paths(self.project_path_instance.get_project_path(), 'output_files')
        for file_name in dir_list(output_files_path):
            if file_name.endswith('.sof'):
                return join_paths(output_files_path, file_name)
        return None
