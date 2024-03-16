from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


class OutputTerminalController(QObject):
    _instance = None

    def __init__(self, output_terminal):
        super(OutputTerminalController, self).__init__()

        if self.__class__._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.output_terminal = output_terminal

    def write_text(self, text):
        self.output_terminal.clear()
        self.output_terminal.appendPlainText(text)

    def append_text(self, text):
        current_text = self.output_terminal.toPlainText()
        self.output_terminal.setPlainText(current_text + text)

    def get_terminal_content(self):
        return self.output_terminal.toPlainText()
