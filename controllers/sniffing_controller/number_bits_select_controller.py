from PyQt5.QtCore import QObject


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
            raise Exception("An instance of NumberBitsSelectController already exists. Use get_instance() to access it.")

        self.number_bit_select = number_bit_select
        self.bits_input_dialog = bits_input_dialog
        self.number_bits = None

        self.handle_selection()

    def handle_selection(self):
        self.number_bit_select.bits_combo.activated.connect(self.check_bits_selection)

    def check_bits_selection(self):
        selected_option = self.number_bit_select.get_selected_pin_number()

        if selected_option == "NBits":
            label_text = "Enter number of bits (PIPO): "
            self.open_bits_dialog(label_text)
        elif selected_option == "1Bit":
            label_text = "Enter number of output bits (SIPO): "
            self.open_bits_dialog(label_text)

    def open_bits_dialog(self, label_text):
        self.bits_input_dialog.bits_label.setText(label_text)
        self.bits_input_dialog.exec_()
