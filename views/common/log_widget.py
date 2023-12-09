from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPlainTextEdit
from loguru import logger


class LogWidget(QPlainTextEdit):

    class QtHandler:
        def write(self, message):
            self.widget.appendPlainText(message.rstrip())

        def __init__(self, widget):
            self.widget = widget

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setup_logger()
        self.insertPlainText("Welcome to ESSET\n")

    def init_ui(self):
        self.setReadOnly(True)
        self.setFont(QFont("monospace", 10))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def setup_logger(self):
        handler = self.QtHandler(self)
        logger.remove()
        logger.add(handler.write, level="DEBUG")