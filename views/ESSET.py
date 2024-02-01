import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (NavigationBar, NavigationItemPosition, isDarkTheme)
from qframelesswindow import FramelessWindow

from views.common.log_widget import LogWidget
from views.common.settings_menu import SettingsMenu
from views.custom_component.custom_title_bar import CustomTitleBar
from views.custom_component.stacked_widget import StackedWidget
from views.display.display_widget import DisplayWidget
from views.sniffing.sniffing_widget import SniffingWidget


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBar(CustomTitleBar(self))

        self.layout = QHBoxLayout(self)
        self.navigation_bar = NavigationBar(self)
        self.stack_widget = StackedWidget(self)
        self.log = LogWidget()

        self.sniffing_widget = SniffingWidget(self)
        self.sniffing_widget.setObjectName("Sniffing Widget")
        self.display_widget = DisplayWidget()
        self.display_widget.setObjectName("Display Widget")
        self.settings_menu = SettingsMenu(self)

        self.init_ui()
        self.init_navigation()
        self.init_window()
        self.log.open_new_log()

    def init_ui(self):
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 48, 0, 0)
        self.layout.addWidget(self.navigation_bar)
        self.layout.addWidget(self.stack_widget)
        self.layout.setStretchFactor(self.stack_widget, 1)

    def init_navigation(self):
        self.addSubInterface(self.sniffing_widget, QIcon('../assets/icons/sniffing.svg'), 'Sniffing')
        self.addSubInterface(self.display_widget, QIcon('../assets/icons/display.svg'), 'Display')
        self.navigation_bar.addItem(
            routeKey='Settings Button',
            icon=FIF.SETTING,
            text='Settings',
            onClick=self.settings_menu.open_settings_menu,
            position=NavigationItemPosition.BOTTOM,
        )

        self.stack_widget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.navigation_bar.setCurrentItem(self.sniffing_widget.objectName())

    def init_window(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('ESSET')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)
        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, selectedIcon=None):
        self.stack_widget.addWidget(interface)
        self.navigation_bar.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            selectedIcon=selectedIcon,
            position=position,
        )

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'../assets/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        self.stack_widget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stack_widget.widget(index)
        self.navigation_bar.setCurrentItem(widget.objectName())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    app.exec_()
