from PyQt5.QtGui import QTextCursor

from models.log_messages import instance_exists_error


class TerminalController:
    _instance = None
    PREFIX_COLORS = {
        'Info': 'darkgreen',
        'Warning': 'Goldenrod',
        'Error': 'red',
    }

    @staticmethod
    def get_instance(terminal=None):
        if TerminalController._instance is None:
            TerminalController._instance = TerminalController(terminal)
        return TerminalController._instance

    def __init__(self, terminal):
        super(TerminalController, self).__init__()

        if TerminalController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.terminal = terminal

    def write_text(self, text):
        self.clear_terminal()
        self.terminal.insertPlainText(text)

    def clear_terminal(self):
        self.terminal.clear()

    def append_line(self, line):
        color = 'darkblue'
        for prefix, prefix_color in self.PREFIX_COLORS.items():
            if line.startswith(prefix):
                color = prefix_color
                break
        self.append_colored_text(line, color)

    def append_colored_text(self, text, color):
        cursor = self.terminal.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertHtml(f'<font color="{color}">{text}</font><br>')
        self.terminal.setTextCursor(cursor)
        self.terminal.ensureCursorVisible()
