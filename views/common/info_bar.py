from PyQt5.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition


def create_info_bar(parent, title, content):
    InfoBar.info(
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=3000,
        parent=parent
    )


def create_success_bar(parent, title, content):
    InfoBar.success(
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=3000,
        parent=parent
    )


def create_warning_bar(parent, title, content):
    InfoBar.warning(
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=3000,
        parent=parent
    )


def create_error_bar(parent, title, content):
    InfoBar.error(
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=True,
        position=InfoBarPosition.BOTTOM_LEFT,
        duration=3000,
        parent=parent
    )
