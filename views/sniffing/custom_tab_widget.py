from PyQt5.QtWidgets import QTabWidget, QTabBar


class QCustomTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(QCustomTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)
        self.hideCloseButtonForLastTab()

    def hideCloseButtonForLastTab(self):
        lastTabIndex = self.count() - 1
        if lastTabIndex >= 0:
            self.tabBar().setTabButton(lastTabIndex, QTabBar.RightSide, None)

    def addTab(self, widget, label):
        super(QCustomTabWidget, self).addTab(widget, label)
        self.hideCloseButtonForLastTab()

    def closeTab(self, index):
        from views.sniffing.vhdl_editor import VhdlEditor
        VhdlEditor.flag_close = True
        currentQWidget = self.widget(index)
        currentQWidget.deleteLater()
        self.removeTab(index)
        self.hideCloseButtonForLastTab()
