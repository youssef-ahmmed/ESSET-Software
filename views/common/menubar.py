from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QAction, QMenuBar, QFileDialog


class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        file_menu = self.addMenu('File')

        add_new_path_action = QAction('Add New Path', self)
        add_new_path_action.setShortcut('Ctrl+O')
        add_new_path_action.triggered.connect(self.open_directory_dialog)
        file_menu.addAction(add_new_path_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close_application)
        file_menu.addAction(exit_action)

    def open_directory_dialog(self):
        directory_path = QFileDialog.getExistingDirectory(self, 'Select Project Directory')
        if directory_path:
            print(directory_path)

    @staticmethod
    def close_application():
        QApplication.instance().quit()
