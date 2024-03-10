from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import RoundMenu, Action, MenuAnimationType

from controllers.operations_controller.receive_data_action_controller import ReceiveDataActionController
from controllers.operations_controller.replay_attack_action_controller import ReplayAttackActionController
from controllers.operations_controller.sniffing_action_controller import SniffingActionController
from controllers.operations_controller.stream_finder_action_controller import StreamFinderActionController
from controllers.project_path_controller import ProjectPathController
from models import log_messages
from views.common.info_bar import create_error_bar


class OperationsButton(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.operations_menu = RoundMenu()

        self.init_ui()
        # self.start_communication()

    def init_ui(self):
        self.sniffing_action = Action(FIF.ROBOT, 'Sniffing Data', shortcut='Ctrl+n')
        self.receive_data_action = Action(FIF.FOLDER_ADD, 'Receive Data', shortcut='Ctrl+r')
        self.replay_attack_action = Action(FIF.SEND_FILL, 'Replay Attack', shortcut='Ctrl+a')
        self.stream_finder_action = Action(FIF.SEARCH_MIRROR, 'Stream Finder', shortcut='Ctrl+f')

        self.operations_menu.addActions([self.sniffing_action, self.receive_data_action,
                                         self.replay_attack_action, self.stream_finder_action])

    def open_operations_menu(self):
        if not ProjectPathController.get_instance().is_project_path_exists():
            create_error_bar(log_messages.NO_QUARTUS_PATH)
            return

        screen_geometry = QApplication.desktop().availableGeometry()
        y = screen_geometry.height() - self.height()
        self.operations_menu.exec(QPoint(80, y), aniType=MenuAnimationType.DROP_DOWN)

    def start_communication(self):
        self.sniffing_action.triggered.connect(lambda: SniffingActionController())
        self.receive_data_action.triggered.connect(lambda: ReceiveDataActionController())
        self.replay_attack_action.triggered.connect(lambda: ReplayAttackActionController())
        self.stream_finder_action.triggered.connect(lambda: StreamFinderActionController())
