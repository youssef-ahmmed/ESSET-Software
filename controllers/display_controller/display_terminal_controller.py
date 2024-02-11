from PyQt5.QtCore import QObject


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
            raise Exception("An instance of DisplayTerminalController already exists. Use get_instance() to access it.")

        self.display_terminal = display_terminal

    def write_text(self, text):
        self.display_terminal.clear()
        self.display_terminal.appendPlainText(text)

    def append_text(self, text):
        self.display_terminal.clear()
        self.display_terminal.appendPlainText(text)
