from PyQt5.QtCore import QObject


class CommProtocolSelectController(QObject):

    _instance = None

    @staticmethod
    def get_instance(comm_protocol_select=None):
        if CommProtocolSelectController._instance is None:
            CommProtocolSelectController._instance = CommProtocolSelectController(comm_protocol_select)
        return CommProtocolSelectController._instance

    def __init__(self, comm_protocol_select):
        super(CommProtocolSelectController, self).__init__()

        if CommProtocolSelectController._instance is not None:
            raise Exception("An instance of CommProtocolSelectController already exists. Use get_instance() to access it.")

        self.comm_protocol_select = comm_protocol_select

    def get_selected_option(self):
        return self.comm_protocol_select.get_selected_protocol()

    def reset_comm_protocol_selection(self):
        self.comm_protocol_select.reset_selected_protocol()
