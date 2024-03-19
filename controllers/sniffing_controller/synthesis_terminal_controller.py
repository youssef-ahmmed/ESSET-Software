from controllers.abstract_controller.output_terminal_controller import OutputTerminalController


class SynthesisTerminalController(OutputTerminalController):

    _instance = None

    @staticmethod
    def get_instance(synthesis_terminal=None):
        if SynthesisTerminalController._instance is None:
            SynthesisTerminalController._instance = SynthesisTerminalController(synthesis_terminal)
        return SynthesisTerminalController._instance

    def __init__(self, synthesis_terminal):
        super(SynthesisTerminalController, self).__init__(synthesis_terminal)
