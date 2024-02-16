from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


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
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.comm_protocol_select = comm_protocol_select

    def get_selected_option(self):
        return self.comm_protocol_select.get_selected_protocol()
