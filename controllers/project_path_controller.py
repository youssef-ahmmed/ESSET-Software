from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QFileDialog


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

    def get_project_path(self):
        return self.project_path
