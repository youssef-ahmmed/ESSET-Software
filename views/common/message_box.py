from PyQt5.QtWidgets import QMessageBox, QWidget
from loguru import logger

from controllers.project_path_controller import ProjectPathController
from models import log_messages


class MessageBox(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setGeometry(300, 300, 300, 220)

    @staticmethod
    def show_project_path_error_dialog(parent):
        reply = QMessageBox.question(parent, 'Error',
                                     'There is No Quartus Path Specified\n\nDo You Want to specify one?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            ProjectPathController.get_instance().open_directory_dialog()
        else:
            logger.warning(log_messages.NO_QUARTUS_PATH)
