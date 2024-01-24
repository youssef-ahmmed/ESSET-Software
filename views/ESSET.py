import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSplitter
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QApplication

from views.common.log_widget import LogWidget
from views.common.menubar import MenuBar
from views.display.display_widget import DisplayWidget
from views.sniffing.sniffing_widget import SniffingWidget


class ESSET(QMainWindow):

    def __init__(self):
        super().__init__()
        self.menu_bar = MenuBar()
        self.tab_widget = QTabWidget()
        self.log = LogWidget()

        self.init_ui()
        self.log.open_new_log()

    def init_ui(self):
        self.setMenuBar(self.menu_bar)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.tab_widget.setTabPosition(QTabWidget.West)
        self.tab_widget.addTab(SniffingWidget(), 'Sniffing')
        self.tab_widget.addTab(DisplayWidget(), 'Display')

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.tab_widget)
        splitter.addWidget(self.log)
        splitter.setSizes([9, 1])

        layout.addWidget(splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ESSET()
    window.showMaximized()
    sys.exit(app.exec_())
