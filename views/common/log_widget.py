import os
from datetime import datetime

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication
from loguru import logger
from qfluentwidgets import MenuAnimationType, RoundMenu, PlainTextEdit


class LogWidget(QWidget):
    LOG_DIR = '../Logging'

    def __init__(self, parent=None):
        super().__init__(parent)

        self.log = PlainTextEdit()
        self.log_menu = RoundMenu()

        self.init_ui()
        self.setup_logger()

    def init_ui(self):
        self.log.setReadOnly(True)
        self.log.setFont(QFont("monospace", 10))
        self.log.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.log.setMinimumWidth(800)
        self.log_menu.addWidget(self.log)

    def open_log_widget(self):
        screen_geometry = QApplication.desktop().availableGeometry()
        y = screen_geometry.height() - self.height()
        self.log_menu.exec(QPoint(80, y), aniType=MenuAnimationType.FADE_IN_PULL_UP)

    def setup_logger(self):
        handler = self.QtHandler(self.log)
        logger.remove()
        logger.add(handler.write, level="DEBUG", format="{time:D-MM-YYYY  HH:mm:ss} | {level} | {message}")

    @staticmethod
    def open_new_log():
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")
        file_path = os.path.join(LogWidget.LOG_DIR, f"ESSET-LOG_{formatted_datetime}.log")
        if not os.path.isdir(LogWidget.LOG_DIR):
            os.mkdir(LogWidget.LOG_DIR)
        logger.add(file_path, level="DEBUG", format="{time:D-MM-YYYY  HH:mm:ss} | {level} | {message}")

    class QtHandler:
        COLORS = {
            "INFO": {"background": "lightblue", "text": "blue"},
            "SUCCESS": {"background": "lightgreen", "text": "green"},
            "WARNING": {"background": "lightyellow", "text": "Goldenrod"},
            "ERROR": {"background": "lightcoral", "text": "red"},
        }

        def __init__(self, widget):
            self.widget = widget

        def write(self, message):
            parts = message.split(" | ")
            level = parts[1].strip()

            color_styles = self.COLORS.get(level, {"background": "white", "text": "black"})
            text_color = color_styles["text"]
            background_color = color_styles["background"]

            formatted_message = (
                f'<span style="color:{text_color}"><b>{parts[0]} | </b></span>'
                f'<span style="background-color:{background_color};color:{text_color}">'
                f'<b>{parts[1]}</b></span>'
                f'<span style="color:{text_color}"><b> | {parts[2]}</b></span>'
            )
            self.widget.appendHtml(formatted_message)
