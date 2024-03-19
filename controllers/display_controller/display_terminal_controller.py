from controllers.abstract_controller.output_terminal_controller import OutputTerminalController


class DisplayTerminalController(OutputTerminalController):

    _instance = None

    @staticmethod
    def get_instance(display_terminal=None):
        if DisplayTerminalController._instance is None:
            DisplayTerminalController._instance = DisplayTerminalController(display_terminal)
        return DisplayTerminalController._instance

    def __init__(self, display_terminal):
        super(DisplayTerminalController, self).__init__(display_terminal)
