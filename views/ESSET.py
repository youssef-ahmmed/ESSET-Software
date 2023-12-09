import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSplitter
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QApplication
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout

from views.display.display_widget import DisplayWidget
from views.sniffing.sniffing_widget import SniffingWidget


class ESSET(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction('Open')
        file_menu.addAction('Save')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.init_tabs()

        plain_text_edit = QPlainTextEdit()
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.tab_widget)
        splitter.addWidget(plain_text_edit)

        splitter.setSizes([9, 1])

        layout.addWidget(splitter)

    def init_tabs(self):
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        sniffing_tab = SniffingWidget()
        self.tab_widget.addTab(sniffing_tab, 'Sniffing')

        display_tab = DisplayWidget()
        self.tab_widget.addTab(display_tab, 'Display')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ESSET()
    window.showMaximized()
    sys.exit(app.exec_())
