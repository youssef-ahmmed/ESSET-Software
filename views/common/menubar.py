from PyQt5.QtWidgets import QApplication, QAction, QMenuBar

from controller.project_path_controller import ProjectPathController


class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.file_menu = self.addMenu('File')

        self.add_new_path_action = QAction('Add New Path', self)
        self.add_new_path_action.setShortcut('Ctrl+O')
        self.file_menu.addAction(self.add_new_path_action)

        self.exit_action = QAction('Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.file_menu.addAction(self.exit_action)

    def start_communication(self):
        self.add_new_path_action.triggered.connect(
            lambda: ProjectPathController.get_instance().open_directory_dialog()
        )
        self.exit_action.triggered.connect(lambda: QApplication.instance().quit())
