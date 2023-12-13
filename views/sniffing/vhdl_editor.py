import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTabWidget, QLabel, QVBoxLayout, QWidget

from views.sniffing.editor.editor import Editor
from views.sniffing.editor.highlighter import Highlighter


class VhdlEditor(QWidget):

    editor_tab_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super(VhdlEditor, self).__init__(parent)
        self.tab_widget = QTabWidget(self)
        self.editor = Editor(self)
        self.editor_index = 0
        self.editor_list = [self.editor]
        self.project_path_label = QLabel("Quartus Project Path: ")
        self.highlighter = Highlighter(self.editor.document())

        self.init_ui()
        self.start_communication()

    def init_ui(self):
        self.setLayout(QVBoxLayout())

        self.tab_widget.addTab(self.editor, 'Untitled')
        self.tab_widget.addTab(QWidget(), '+')
        self.tab_widget.setTabEnabled(-1, False)

        self.layout().addWidget(self.tab_widget)
        self.layout().addWidget(self.project_path_label)

    def start_communication(self):
        self.tab_widget.currentChanged.connect(self.emit_editor_tab_changed)
        self.tab_widget.currentChanged.connect(self.tab_changed)

    def emit_editor_tab_changed(self, index):
        if index != self.tab_widget.count() - 1:
            self.editor_index = index
            self.editor_tab_changed.emit(index)

    def tab_changed(self, index):
        if index == self.tab_widget.count() - 1:
            self.add_blank_editor_tab()

    def add_blank_editor_tab(self):
        new_editor = Editor(self)
        Highlighter(new_editor.document())
        self.editor_list.append(new_editor)

        tab_index = self.tab_widget.count() - 1
        self.tab_widget.insertTab(tab_index, new_editor, f'Untitled{tab_index}')
        self.tab_widget.setCurrentIndex(tab_index)

    def update_project_path_label(self, project_path):
        self.project_path_label.setText(f"Quartus Project Path: {project_path}")

    def change_editor_label(self, index, file_name):
        file_name = os.path.basename(file_name)
        self.tab_widget.setTabText(index, file_name)
