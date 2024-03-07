from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import RoundMenu, Action, MenuAnimationType

from controllers.environment_path_controller import EnvironmentPathController
from controllers.project_path_controller import ProjectPathController


class SettingsMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.menu = RoundMenu()

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.new_project_path_action = Action(FIF.COMMAND_PROMPT, 'New Project Path', shortcut='Ctrl+o')
        self.set_env_path_action = Action(FIF.DEVELOPER_TOOLS, 'Set Environment Path', shortcut='Ctrl+e')
        self.menu.addActions([self.new_project_path_action, self.set_env_path_action])

        self.menu.addSeparator()
        self.menu.addAction(Action(FIF.FEEDBACK, 'Feedback', shortcut='Ctrl+F'))
        self.menu.addAction(Action(FIF.HELP, 'Help', shortcut='Ctrl+H'))

    def open_settings_menu(self):
        screen_geometry = QApplication.desktop().availableGeometry()
        y = screen_geometry.height() - self.height()
        self.menu.exec(QPoint(80, y), aniType=MenuAnimationType.DROP_DOWN)

    def start_communication(self):
        self.new_project_path_action.triggered.connect(ProjectPathController.get_instance().open_project_path_dialog)
        self.set_env_path_action.triggered.connect(EnvironmentPathController.get_instance().open_env_path_dialog)
