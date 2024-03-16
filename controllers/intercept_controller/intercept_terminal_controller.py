from controllers.abstract_controller.output_terminal_controller import OutputTerminalController


class InterceptTerminalController(OutputTerminalController):

    _instance = None

    @staticmethod
    def get_instance(intercept_terminal=None):
        if InterceptTerminalController._instance is None:
            InterceptTerminalController._instance = InterceptTerminalController(intercept_terminal)
        return InterceptTerminalController._instance

    def __init__(self, intercept_terminal):
        super(InterceptTerminalController, self).__init__(intercept_terminal)
