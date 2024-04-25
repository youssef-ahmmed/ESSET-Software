from controllers.abstract_controller.output_terminal_controller import OutputTerminalController


class FuzzingTerminalController(OutputTerminalController):
    _instance = None

    @staticmethod
    def get_instance(fuzzing_terminal=None):
        if FuzzingTerminalController._instance is None:
            FuzzingTerminalController._instance = FuzzingTerminalController(fuzzing_terminal)
        return FuzzingTerminalController._instance

    def __init__(self, fuzzing_terminal):
        super(FuzzingTerminalController, self).__init__(fuzzing_terminal)
