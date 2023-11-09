from PyQt5.QtCore import QSize, Qt, QRect, QPoint, QRegExp
from PyQt5.QtGui import QKeySequence, QTextCharFormat, QBrush, QColor, QFont, QTextFormat, QPainter, QWheelEvent, \
    QKeyEvent, QTextCursor
from PyQt5.QtWidgets import QPlainTextEdit, QWidget, QAction, QTextEdit, QMenu, QLineEdit


class Editor(QPlainTextEdit):

    class _NumberArea(QWidget):
        def __init__(self, editor):
            super().__init__(editor)
            self.codeEditor = editor

        def sizeHint(self):
            return QSize(self.editor.line_number_area_width(), 0)

        def paintEvent(self, event):
            self.codeEditor.line_number_area_paint_event(event)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = Editor._NumberArea(self)
        self.create_save_action()
        self.create_comment_action()
        self.create_uncomment_action()
        self.create_zoom_in_action()
        self.create_zoom_out_action()
        self.reset_font()

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.update_line_number_area_width(0)
        self.findHighlightFormat = QTextCharFormat()
        self.findHighlightFormat.setBackground(QBrush(QColor("red")))
        self.searchTxtBx = None
        self.currentIndex = -1
        self.currentPattern = None

    def create_save_action(self):
        self.saveACT = QAction("Save")
        self.saveACT.setShortcut(QKeySequence("Ctrl+S"))
        self.saveACT.triggered.connect(lambda: self._save_file(self.toPlainText()))
        self.addAction(self.saveACT)

    def create_comment_action(self):
        self.comment_all_action = QAction("Comment")
        self.comment_all_action.setShortcut(QKeySequence("Ctrl+R"))
        self.addAction(self.comment_all_action)
        self.comment_all_action.triggered.connect(self.comment)

    def create_uncomment_action(self):
        self.uncomment_all_action = QAction("Uncomment")
        self.uncomment_all_action.setShortcut(QKeySequence("Ctrl+Shift+R"))
        self.addAction(self.uncomment_all_action)
        self.uncomment_all_action.triggered.connect(self.uncomment)

    def create_zoom_in_action(self):
        self.zoom_in_action = QAction("Zoom in")
        zoom_in_shortcut = QKeySequence(Qt.Key_Control + Qt.Key_Plus)
        self.zoom_in_action.setShortcut(zoom_in_shortcut)
        self.addAction(self.zoom_in_action)
        self.zoom_in_action.triggered.connect(self.my_zoom_in)

    def create_zoom_out_action(self):
        self.zoom_out_action = QAction("Zoom out")
        zoom_out_shortcut = QKeySequence(Qt.Key_Control + Qt.Key_Minus)
        self.zoom_out_action.setShortcut(zoom_out_shortcut)
        self.addAction(self.zoom_out_action)
        self.zoom_out_action.triggered.connect(self.my_zoom_out)

    def reset_font(self):
        my_font: QFont = QFont("Courier New", 11)
        self.setFont(my_font)

    def line_number_area_width(self):
        digits = 5
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor(229, 248, 255, 255)
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.lineNumberArea)
        blockColor = QColor(233,233,233)
        painter.fillRect(event.rect(), blockColor)
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        fontColor = QColor(200,200,200)
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                fFont = QFont("Courier New", 10)
                painter.setPen(fontColor)
                painter.setFont(fFont)
                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignCenter, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def contextMenuEvent(self, event):
        menu: QMenu = self.createStandardContextMenu()
        if self._addSaveAction:
            index = 0
            if len(menu.actions()) > 6: index = 5
            act_beforeACT = menu.actions()[index]
            menu.insertAction(act_beforeACT, self.saveACT)

        menu.addSeparator()

        comment_pos = menu.actions()[9]
        menu.insertAction(comment_pos, self.comment_all_action)

        uncomment_pos = menu.actions()[10]
        menu.insertAction(uncomment_pos, self.uncomment_all_action)

        menu.addSeparator()

        zoom_in_action = menu.addAction("Increase font size" + "\t" + "Ctrl+Plus sign (+)")
        zoom_in_action.triggered.connect(self.my_zoom_in)

        zoom_out_action = menu.addAction("Decrease font size" + "\t" + "Ctrl+Minus sign (-)")
        zoom_out_action.triggered.connect(self.my_zoom_out)

        reset_font_size_action = menu.addAction("Reset font size")
        reset_font_size_action.triggered.connect(self._reset_font)

        menu.addSeparator()

        find_action = menu.addAction("Find" + "\t" + "Ctrl+F")
        find_action.triggered.connect(self.find_key)
        menu.popup(event.globalPos())

    def my_zoom_in(self):
        self.zoomIn(1)

    def my_zoom_out(self):
        self.zoomOut(1)

    def comment(self):
        txt = self.textCursor().selectedText()
        txt_after_comment = ""
        for line in txt.splitlines():
            txt_after_comment += "//" + line + "\n"
        txt_after_comment = txt_after_comment[:-1]
        cursor = self.textCursor()
        if cursor.hasSelection():
            cursor.insertText(txt_after_comment)

    def uncomment(self):
        txt = self.textCursor().selectedText()
        txt_after_uncomment = ""
        for line in txt.splitlines():
            txt_after_uncomment += line.replace("//", "", 1) + "\n"
        txt_after_uncomment = txt_after_uncomment[:-1]
        cursor = self.textCursor()
        if cursor.hasSelection():
            cursor.insertText(txt_after_uncomment)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.my_zoom_in()
            else:
                self.my_zoom_out()
            event.accept()
        else:
            super().wheelEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_F and (event.modifiers() & Qt.ControlModifier):
            self.find_key()
        elif event.key() == Qt.Key_Plus and (event.modifiers() & Qt.ControlModifier):
            self.my_zoom_in()
        elif event.key() == Qt.Key_Minus and (event.modifiers() & Qt.ControlModifier):
            self.my_zoom_out()
        elif event.key() == Qt.Key_Z and (event.modifiers() & Qt.ControlModifier):
            super().keyPressEvent(event)
            self.check_if_unsaved_changes_signal.emit()
        elif event.key() == Qt.Key_Escape:
            if self.searchTxtBx is not None:
                self.searchTxtBx.hide()
                self.searchTxtBx = None
                self.clear_format()
        elif self.searchTxtBx is not None:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.next_pattern()
                event.ignore()
            else:
                super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def find_key(self):
        if self.searchTxtBx is None:
            self.searchTxtBx = QLineEdit(self)
            p = self.geometry().topRight() - self.searchTxtBx.geometry().topRight() - QPoint(50, 0)
            self.searchTxtBx.move(p)
            self.searchTxtBx.show()
            self.searchTxtBx.textChanged.connect(self.find_with_pattern)
        self.searchTxtBx.setFocus()

    def find_with_pattern(self, pattern):
        self.setUndoRedoEnabled(False)
        self.clear_format()
        if pattern == "":
            return
        cursor = self.textCursor()
        regex = QRegExp(pattern)
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        self.currentIndex = index
        while index != -1:
            cursor.setPosition(index)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            cursor.mergeCharFormat(self.findHighlightFormat)
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)
        if self.currentIndex != -1:
            cursor.setPosition(self.currentIndex)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            self.setTextCursor(cursor)
        self.setUndoRedoEnabled(True)
        self.currentPattern = pattern

    def next_pattern(self):
        self.setUndoRedoEnabled(False)
        if self.currentIndex == -1 and self.currentPattern is not None:
            return
        cursor = self.textCursor()
        regex = QRegExp(self.currentPattern)
        pos = self.currentIndex + regex.matchedLength()
        self.currentIndex = regex.indexIn(self.toPlainText(), pos)
        pos = self.currentIndex + regex.matchedLength()
        self.currentIndex = regex.indexIn(self.toPlainText(), pos)
        if self.currentIndex != -1:
            cursor.setPosition(self.currentIndex)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            self.setTextCursor(cursor)
        else:
            self.currentIndex = regex.indexIn(self.toPlainText(), 0)
            cursor.setPosition(self.currentIndex)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            self.setTextCursor(cursor)
        self.setUndoRedoEnabled(True)

    def clear_format(self):
        cursor = self.textCursor()
        pos = cursor.position()
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(QTextCharFormat())
        cursor.clearSelection()
        cursor.setPosition(pos)
        self.setTextCursor(cursor)
        self.currentIndex = -1
        self.currentPattern = None

    def setSaveCB(self, cb):
        self._saveCB = cb

    def _save_file(self, text):
        if self._saveCB is not None:
            self._saveCB(text)
