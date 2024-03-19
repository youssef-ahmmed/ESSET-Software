from PyQt5.QtCore import QObject
from PyQt5.QtGui import QTextCursor

from models.log_messages import instance_exists_error


class OutputTerminalController(QObject):
    _instance = None
    PREFIX_COLORS = {
        'Info': 'darkgreen',
        'Warning': 'Goldenrod',
        'Error': 'red',
    }

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

    def clear_terminal(self):
        self.output_terminal.clear()

    def append_line(self, line):
        color = 'darkblue'
        for prefix, prefix_color in self.PREFIX_COLORS.items():
            if line.startswith(prefix):
                color = prefix_color
                break
        self.append_colored_text(line, color)

    def append_colored_text(self, text, color):
        cursor = self.output_terminal.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertHtml(f'<font color="{color}">{text}</font><br>')
        self.output_terminal.setTextCursor(cursor)
        self.output_terminal.ensureCursorVisible()
