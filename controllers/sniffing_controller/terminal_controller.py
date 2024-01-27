class TerminalController:
    _instance = None

    @staticmethod
    def get_instance(terminal=None):
        if TerminalController._instance is None:
            TerminalController._instance = TerminalController(terminal)
        return TerminalController._instance

    def __init__(self, terminal):
        super(TerminalController, self).__init__()

        if TerminalController._instance is not None:
            raise Exception("An instance of TerminalController already exists. Use get_instance() to access it.")

        self.terminal = terminal

    def write_text(self, text):
        self.terminal.clear()
        self.terminal.insertPlainText(text)

    def append_line(self, line):
        self.terminal.appendPlainText(line)

    def clear_terminal(self):
        self.terminal.clear()
