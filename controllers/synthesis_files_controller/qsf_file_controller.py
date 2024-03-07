from PyQt5.QtCore import QObject

from PyQt5.QtCore import QObject

from controllers.project_path_controller import ProjectPathController
from models.log_messages import instance_exists_error
from reusable_functions.os_operations import dir_list, split_pathname, join_paths


class QsfFileController(QObject):

    _instance = None

    @staticmethod
    def get_instance():
        if QsfFileController._instance is None:
            QsfFileController._instance = QsfFileController()
        return QsfFileController._instance

    def __init__(self):
        super(QsfFileController, self).__init__()
        if QsfFileController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.project_path = ProjectPathController.get_instance().get_project_path()

    def get_qsf_file_path(self) -> str | None:
        for file_name in dir_list(self.project_path):
            if file_name.endswith('.qsf'):
                return join_paths(self.project_path, file_name)
        return None
