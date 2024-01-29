from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QPushButton, QMessageBox

from controllers.project_path_controller import ProjectPathController
from controllers.sniffing_controller.dialogs_controller.sniffing_timer_controller import SniffingTimerDialogController


class StartSniffingButtonController(QObject):
    _instance = None

    @staticmethod
    def get_instance(start_sniffing_button: QPushButton = None) -> None:
        if StartSniffingButtonController._instance is None:
            StartSniffingButtonController._instance = StartSniffingButtonController(start_sniffing_button)
        return StartSniffingButtonController._instance

    def __init__(self, start_sniffing_button: QPushButton) -> None:
        super(StartSniffingButtonController, self).__init__()

        if StartSniffingButtonController._instance is not None:
            raise Exception("An instance of StartSniffingButtonController already exists. "
                            "Use get_instance() to access it.")

        self.start_sniffing_button = start_sniffing_button
        self.project_path_controller = ProjectPathController.get_instance()

        self.start_communication()

    def start_communication(self) -> None:
        self.start_sniffing_button.clicked.connect(self.check_sof_file)

    def check_sof_file(self) -> None:
        if self.project_path_controller.get_sof_file():
            SniffingTimerDialogController.get_instance().show_sniffing_timer_dialog()
        else:
            QMessageBox.warning(None, "Warning", f"There is no sof file after Synthesis")
