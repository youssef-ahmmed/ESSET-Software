from PyQt5.QtWidgets import QTabWidget, QTabBar


class CustomTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(CustomTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
        self.hide_close_button_for_last_tab()

    def hide_close_button_for_last_tab(self):
        last_tab_index = self.count() - 1
        if last_tab_index >= 0:
            self.tabBar().setTabButton(last_tab_index, QTabBar.RightSide, None)

    def addTab(self, widget, label):
        super(CustomTabWidget, self).addTab(widget, label)
        self.hide_close_button_for_last_tab()

    def close_tab(self, index):
        from views.sniffing.vhdl_editor import VhdlEditor
        VhdlEditor.flag_close = True
        current_widget = self.widget(index)
        current_widget.deleteLater()
        self.removeTab(index)
        self.hide_close_button_for_last_tab()
