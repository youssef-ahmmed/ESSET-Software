from PyQt5.QtCore import Qt
from loguru import logger
from qfluentwidgets import InfoBar, InfoBarPosition


class MainWindowManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._main_window = None
        return cls._instance

    @property
    def main_window(self):
        return self._main_window

    @main_window.setter
    def main_window(self, window):
        self._main_window = window


main_window_manager = MainWindowManager()


def _create_bar(title, content, log_level, info_bar_func):
    main_window = main_window_manager.main_window
    if main_window is None:
        logger.warning("Main window is not set. Please set it using main_window_manager.main_window setter.")
        return

    log_function = getattr(logger, log_level.lower(), logger.info)
    log_function(content)

    info_bar_func(
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=3000,
        parent=main_window
    )


def create_info_bar(content):
    _create_bar("INFO", content, "info", InfoBar.info)


def create_success_bar(content):
    _create_bar("SUCCESS", content, "success", InfoBar.success)


def create_warning_bar(content):
    _create_bar("WARNING", content, "warning", InfoBar.warning)


def create_error_bar(content):
    _create_bar("ERROR", content, "error", InfoBar.error)
