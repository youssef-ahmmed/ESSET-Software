from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


class NumberBitsSelectController(QObject):

    _instance = None

    @staticmethod
    def get_instance(number_bit_select=None, input_dialog=None):
        if NumberBitsSelectController._instance is None:
            NumberBitsSelectController._instance = NumberBitsSelectController(number_bit_select, input_dialog)
        return NumberBitsSelectController._instance

    def __init__(self, number_bit_select, bits_input_dialog):
        super(NumberBitsSelectController, self).__init__()

        if NumberBitsSelectController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.number_bit_select = number_bit_select
        self.bits_input_dialog = bits_input_dialog
        self.number_bits = None

        self.handle_selection()

    def handle_selection(self):
        self.number_bit_select.bits_combo.currentTextChanged.connect(self.check_bits_selection)

    def check_bits_selection(self):
        self.selected_option = self.number_bit_select.get_selected_pin_number()

        if self.selected_option == "NBits":
            label_text = "Enter number of bits (PIPO): "
            self.open_bits_dialog(label_text)
        elif self.selected_option == "1Bit":
            label_text = "Enter number of output bits (SIPO): "
            self.open_bits_dialog(label_text)

    def open_bits_dialog(self, label_text):
        self.bits_input_dialog.bits_label.setText(label_text)
        self.bits_input_dialog.exec_()

    def get_selected_option(self):
        return self.number_bit_select.get_selected_pin_number()
