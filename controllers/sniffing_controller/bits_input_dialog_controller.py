from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMessageBox


class BitsInputDialogController(QObject):
    _instance = None

    @staticmethod
    def get_instance(bits_input_dialog=None):
        if BitsInputDialogController._instance is None:
            BitsInputDialogController._instance = BitsInputDialogController(bits_input_dialog)
        return BitsInputDialogController._instance

    def __init__(self, bits_input_dialog):
        super(BitsInputDialogController, self).__init__()

        if BitsInputDialogController._instance is not None:
            raise Exception("An instance of BitsInputDialogController already exists. Use get_instance() to access it.")

        self.bits_input_dialog = bits_input_dialog
        self.n_bits = None

        self.handle_buttons()

    def handle_buttons(self):
        self.bits_input_dialog.cancel_button.clicked.connect(self.bits_input_dialog.reject)
        self.bits_input_dialog.save_button.clicked.connect(self.save_clicked)

    def save_clicked(self):
        bits_number = self.get_bits_number()
        if bits_number is not None:
            print(f" number of bits: {bits_number}")
            self.bits_input_dialog.accept()

    def get_bits_number(self):
        no_of_bits = self.bits_input_dialog.bits_input.text()
        if not no_of_bits:
            QMessageBox.warning(self.bits_input_dialog, "Warning", "Please enter the number of bits.")
            return None
        self.bits_input_dialog.bits_input.clear()
        return no_of_bits
