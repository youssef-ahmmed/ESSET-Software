from controllers.abstract_controller.output_terminal_controller import OutputTerminalController


class CustomDataTerminalController(OutputTerminalController):

    _instance = None

    @staticmethod
    def get_instance(custom_data_terminal=None):
        if CustomDataTerminalController._instance is None:
            CustomDataTerminalController._instance = CustomDataTerminalController(custom_data_terminal)
        return CustomDataTerminalController._instance

    def __init__(self, custom_data_terminal):
        super(CustomDataTerminalController, self).__init__(custom_data_terminal)
