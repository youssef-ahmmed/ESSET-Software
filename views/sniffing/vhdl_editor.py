from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabBar

from reusable_functions.os_operations import get_basename
from views.sniffing.custom_tab_widget import CustomTabWidget
from views.sniffing.editor.editor import Editor
from views.sniffing.editor.highlighter import Highlighter


class VhdlEditor(QWidget):
    editor_tab_changed = pyqtSignal(int)
    flag_close = False

    def __init__(self, parent=None):
        super(VhdlEditor, self).__init__(parent)
        self.tab_widget = CustomTabWidget(self)
        self.editor = Editor(self)
        self.editor_index = 0

        self.editor_list = [self.editor]
        self.project_path_label = QLabel("Quartus Project Path: ")
        self.highlighter = [Highlighter(self.editor.document())]

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.tab_widget.addTab(self.editor, 'Untitled')
        self.tab_widget.addTab(QWidget(), '+')
        self.tab_widget.setTabEnabled(-1, False)
        self.tab_widget.tabBar().setTabButton(-1, QTabBar.RightSide, None)

        self.layout().addWidget(self.tab_widget)
        self.layout().addWidget(self.project_path_label)

    def start_communication(self):
        self.tab_widget.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        if (index == self.tab_widget.count() - 1) and (VhdlEditor.flag_close == False):
            self.add_blank_editor_tab()
        VhdlEditor.flag_close = False
        tab_index = self.tab_widget.count() - 2
        self.tab_widget.setCurrentIndex(tab_index)

    def add_blank_editor_tab(self):
        new_editor = Editor(self)
        highlighter = Highlighter(new_editor.document())
        self.editor_list.append(new_editor)
        self.highlighter.append(highlighter)

        tab_index = self.tab_widget.count() - 1
        self.tab_widget.insertTab(tab_index, new_editor, f'Untitled{tab_index}')
        self.tab_widget.setCurrentIndex(tab_index)

    def update_project_path_label(self, project_path):
        self.project_path_label.setText(f"Quartus Project Path: {project_path}")

    def change_editor_label(self, index, file_name):
        file_name = get_basename(file_name)
        self.tab_widget.setTabText(index, file_name)
