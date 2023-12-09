from PyQt5.QtWidgets import QFrame, QTabWidget, QLabel, QVBoxLayout, QWidget

from views.sniffing.editor import Editor
from views.sniffing.editor.highlighter import Highlighter


class VhdlEditor(QFrame):

    def __init__(self, parent=None):
        super(VhdlEditor, self).__init__(parent)
        self.vhdl_editor = Editor(self)
        self.tab_widget = QTabWidget(self)
        self.quartus_directory_path_label = QLabel("Quartus Project Path: ")
        self.quartus_directory_path = ""
        self.highlighter = Highlighter(self.vhdl_editor.document())

        self.init_ui()

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

    def set_tab_closable(self):
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

    def init_ui(self):
        self.tab_widget.addTab(self.vhdl_editor, 'Untitled')
        self.tab_widget.addTab(QWidget(), '+')
        self.tab_widget.setTabEnabled(-1, False)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.tab_widget)
        self.layout().addWidget(self.quartus_directory_path_label)

        self.tab_widget.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        if index == self.tab_widget.count() - 1:
            self.add_blank_editor_tab()

    def add_blank_editor_tab(self):
        new_editor = Editor(self)
        tab_index = self.tab_widget.count() - 1
        self.tab_widget.insertTab(tab_index, new_editor, 'Untitled')
        self.tab_widget.setCurrentIndex(tab_index)
