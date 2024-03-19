from PyQt5.QtCore import QObject

from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController
from models.log_messages import instance_exists_error


class DataOperationController(QObject):
    _instance = None

    @staticmethod
    def get_instance(data_operation_widget=None):
        if DataOperationController._instance is None:
            DataOperationController._instance = DataOperationController(
                data_operation_widget)
        return DataOperationController._instance

    def __init__(self, data_operation_widget):
        super(DataOperationController, self).__init__()

        if DataOperationController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.data_operation_widget = data_operation_widget
        self.start_communication()
    
    def start_communication(self):
        self.data_operation_widget.flip_all_ones.clicked.connect(self.flip_all_ones_to_zeros)
        self.data_operation_widget.flip_all_zeros.clicked.connect(self.flip_all_zeros_to_ones)
        self.data_operation_widget.flip_all_bits.clicked.connect(self.flip_all_bits)

    def flip_bits(self, flip_type):
        hex_str = InterceptTerminalController.get_instance().get_terminal_content()
        hex_str = hex_str.replace('\\x', '')
        byte_arr = bytearray.fromhex(hex_str)

        for i in range(len(byte_arr)):
            if flip_type == 'ones_to_zeros':
                byte_arr[i] = byte_arr[i] & (~byte_arr[i] & 0xFF)
            elif flip_type == 'zeros_to_ones':
                byte_arr[i] = byte_arr[i] | (~byte_arr[i] & 0xFF)
            elif flip_type == 'all':
                byte_arr[i] = byte_arr[i] ^ 0xFF

        flipped_hex = ''.join('\\x{:02x}'.format(byte) for byte in byte_arr)
        InterceptTerminalController.get_instance().write_text(flipped_hex)

    def flip_all_ones_to_zeros(self):
        self.flip_bits('ones_to_zeros')

    def flip_all_zeros_to_ones(self):
        self.flip_bits('zeros_to_ones')

    def flip_all_bits(self):
        self.flip_bits('all')
