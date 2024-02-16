from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


class DisplayTerminalController(QObject):

    _instance = None

    @staticmethod
    def get_instance(display_terminal=None):
        if DisplayTerminalController._instance is None:
            DisplayTerminalController._instance = DisplayTerminalController(display_terminal)
        return DisplayTerminalController._instance

    def __init__(self, display_terminal):
        super(DisplayTerminalController, self).__init__()

        if DisplayTerminalController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.display_terminal = display_terminal

    def write_text(self, text):
        self.display_terminal.clear()
        self.display_terminal.appendPlainText(text)

    def append_text(self, text):
        self.display_terminal.clear()
        self.display_terminal.appendPlainText(text)
