import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QSplitter, QDockWidget
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QApplication
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout
from views.sniffing.sniffing_widget import SniffingWidget


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction('Open')
        file_menu.addAction('Save')

        # Main Widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Tab Widget
        tab_widget = QTabWidget()
        tab_widget.setTabPosition(QTabWidget.West)  # Place the tabs on the left

        tab1 = SniffingWidget()
        # tab2 = Tab2()
        # tab3 = Tab3()
        # tab4 = Tab4()

        tab_widget.addTab(tab1, 'Tab 1')
        # tab_widget.addTab(tab2, 'Tab 2')
        # tab_widget.addTab(tab3, 'Tab 3')
        # tab_widget.addTab(tab4, 'Tab 4')

        plain_text_edit = QPlainTextEdit()
        # plain_text_edit.setMinimumHeight(200)
        # plain_text_edit.setMaximumHeight(500)

        # layout.addWidget(file_menu)
        # layout.addWidget(tab_widget)
        # layout.addWidget(plain_text_edit)




        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(tab_widget)
        splitter.addWidget(plain_text_edit)
        # splitter.addWidget(btn1)
        # splitter.addWidget(btn2)
        # splitter.addWidget(btn3)
        # splitter.addWidget(btn4)
        # splitter.addWidget(btn5)


        layout.addWidget(splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.showMaximized()  # Make the window full screen
    sys.exit(app.exec_())