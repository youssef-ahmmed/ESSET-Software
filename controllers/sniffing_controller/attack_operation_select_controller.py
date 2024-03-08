from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error
from views.sniffing.attack_operation_select import AttackOperationSelect


class AttackOperationSelectController(QObject):

    _instance = None

    @staticmethod
    def get_instance(attack_operation_select: AttackOperationSelect=None):
        if AttackOperationSelectController._instance is None:
            AttackOperationSelectController._instance = AttackOperationSelectController(attack_operation_select)
        return AttackOperationSelectController._instance

    def __init__(self, attack_operation_select: AttackOperationSelect):
        super(AttackOperationSelectController, self).__init__()

        if AttackOperationSelectController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.attack_operation_select = attack_operation_select

    def get_selected_attack_operation(self):
        return self.attack_operation_select.get_selected_option()
