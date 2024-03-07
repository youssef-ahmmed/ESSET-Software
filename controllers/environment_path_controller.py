from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog

from models import log_messages
from models.log_messages import instance_exists_error
from views.common.info_bar import create_success_bar, create_warning_bar


class EnvironmentPathController(QObject):

    _instance = None

    @staticmethod
    def get_instance():
        if EnvironmentPathController._instance is None:
            EnvironmentPathController._instance = EnvironmentPathController()
        return EnvironmentPathController._instance

    def __init__(self):
        super(EnvironmentPathController, self).__init__()
        if EnvironmentPathController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.env_path = ""
        
    def open_env_path_dialog(self):
        path = QFileDialog.getExistingDirectory(None, 'Select Environment Path')
        if path:
            self.env_path = path
            create_success_bar(log_messages.ENV_PATH_SET)
        else:
            create_warning_bar(log_messages.NO_ENV_PATH)

    def get_env_path(self):
        return self.env_path
