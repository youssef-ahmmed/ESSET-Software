from PyQt5.QtCore import QObject

from controllers.intercept_controller.intercept_terminal_controller import InterceptTerminalController


class BytePositionDialogController(QObject):

    def __init__(self, byte_position_dialog):
        super(BytePositionDialogController, self).__init__()

        self.byte_position_dialog = byte_position_dialog
        self.start_communication()
        self.update_bytes_items()

    def start_communication(self):
        self.byte_position_dialog.yesButton.clicked.connect(self.flip_one_byte)

    def update_bytes_items(self):
        byte_positions = []
        data = InterceptTerminalController.get_instance().get_terminal_content()
        for i in range(len(data) // 4):
            byte_positions.append(str(i))
        self.byte_position_dialog.positions.addItems(byte_positions)

    def flip_one_byte(self):
        hex_str = InterceptTerminalController.get_instance().get_terminal_content()
        index = int(self.byte_position_dialog.get_selected_byte())
        hex_str = hex_str.replace('0x', '')
        byte_arr = bytearray.fromhex(hex_str)
        byte_arr[index] = ~byte_arr[index] & 0xFF
        flipped_hex = ''.join('0x{:02x}'.format(byte) for byte in byte_arr)
        InterceptTerminalController.get_instance().write_text(flipped_hex)
