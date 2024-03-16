import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QMessageBox
from qfluentwidgets import FluentIcon as FIF, MessageBox
from qfluentwidgets import (NavigationBar, NavigationItemPosition, isDarkTheme)
from qframelesswindow import FramelessWindow

from views.common.info_bar import main_window_manager
from views.common.log_widget import LogWidget
from views.common.operation_button import OperationsButton
from views.common.settings_menu import SettingsMenu
from views.custom_component.custom_title_bar import CustomTitleBar
from views.custom_component.stacked_widget import StackedWidget
from views.display.display_widget import DisplayWidget
from views.intercept.intercept_widget import InterceptWidget
from views.sniffing.sniffing_widget import SniffingWidget

main_window_manager.main_window = None


class MainWindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        main_window_manager.main_window = self
        self.setTitleBar(CustomTitleBar(self))

        self.layout = QHBoxLayout(self)
        self.navigation_bar = NavigationBar(self)
        self.stack_widget = StackedWidget(self)
        self.log = LogWidget(self)

        self.sniffing_widget = SniffingWidget()
        self.sniffing_widget.setObjectName("Sniffing Widget")
        self.display_widget = DisplayWidget()
        self.display_widget.setObjectName("Display Widget")
        self.intercept_widget = InterceptWidget()
        self.intercept_widget.setObjectName("Intercept Widget")
        self.settings_menu = SettingsMenu(self)
        self.operations_button = OperationsButton(self)

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
        self.add_sub_interface(self.sniffing_widget, QIcon('../assets/icons/config.svg'), 'Config')
        self.add_sub_interface(self.display_widget, QIcon('../assets/icons/display.svg'), 'Display')
        self.add_sub_interface(self.intercept_widget, QIcon('../assets/icons/intercept.png'), 'Intercept')

        self.add_navigatiob_bar_button('Attack Operations', FIF.PLAY_SOLID, 'Operations',
                                       self.operations_button.open_operations_menu, NavigationItemPosition.BOTTOM)
        self.add_navigatiob_bar_button('Log Button', FIF.CALENDAR, 'Log', self.log.open_log_widget,
                                       NavigationItemPosition.BOTTOM)
        self.add_navigatiob_bar_button('Settings Button', FIF.SETTING, 'Settings',
                                       self.settings_menu.open_settings_menu, NavigationItemPosition.BOTTOM)

        self.stack_widget.currentChanged.connect(self.on_current_interface_changed)
        self.navigation_bar.setCurrentItem(self.sniffing_widget.objectName())

    def init_window(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('ESSET')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)
        self.set_qss()

    def add_sub_interface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, selectedIcon=None):
        self.stack_widget.addWidget(interface)
        self.navigation_bar.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switch_to(interface),
            selectedIcon=selectedIcon,
            position=position,
        )
    
    def add_navigatiob_bar_button(self, route_key, icon, text, on_click, position):
        self.navigation_bar.addItem(
            routeKey=route_key,
            icon=icon,
            text=text,
            onClick=on_click,
            position=position
        )

    def set_qss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'../assets/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switch_to(self, widget):
        self.stack_widget.setCurrentWidget(widget)

    def on_current_interface_changed(self, index):
        widget = self.stack_widget.widget(index)
        self.navigation_bar.setCurrentItem(widget.objectName())

        if widget == self.intercept_widget:
            QMessageBox.warning(self, "Warning", "Tool Must Be Connected In Series")
            title = 'Warning'
            content = """Tool Must Be Connected In Series"""
            MessageBox(title, content, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    app.exec_()
