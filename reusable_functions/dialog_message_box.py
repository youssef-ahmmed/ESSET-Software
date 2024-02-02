from PyQt5.QtWidgets import QMessageBox


def show_error_message(widget, message):
    QMessageBox.warning(widget, "Error", message)
