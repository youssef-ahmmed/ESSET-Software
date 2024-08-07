from PyQt5.QtCore import QSize, Qt, QRect, QPoint, QRegExp
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QFont, QTextFormat, QPainter, QWheelEvent, \
    QKeyEvent, QTextCursor
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit
from qfluentwidgets import PlainTextEdit


class Editor(PlainTextEdit):

    class NumberArea(QWidget):
        def __init__(self, editor):
            super().__init__(editor)
            self.editor = editor

        def sizeHint(self):
            return QSize(self.editor.line_number_area_width(), 0)

        def paintEvent(self, event):
            self.editor.line_number_area_paint_event(event)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_number_area = Editor.NumberArea(self)
        self.find_highlight_format = QTextCharFormat()
        self.search_text_box = None
        self.current_index = -1
        self.current_pattern = None
        self.current_file_path = None

        self.start_ui_communication()
        self.reset_font()
        self.update_line_number_area_margin(0)
        self.find_highlight_format.setBackground(QBrush(QColor("green")))

    def start_ui_communication(self):
        self.blockCountChanged.connect(self.update_line_number_area_margin)
        self.updateRequest.connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

    def reset_font(self):
        my_font = QFont("Courier New", 11)
        self.setFont(my_font)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area_width(), cr.height()))

    def line_number_area_paint_event(self, event):
        painter = QPainter(self.line_number_area)
        block_color = QColor(233, 233, 233)
        painter.fillRect(event.rect(), block_color)
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        font_color = QColor(200, 200, 200)
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(block_number + 1)
                font = QFont("Courier New", 11)
                painter.setPen(font_color)
                painter.setFont(font)
                painter.drawText(0, int(top), self.line_number_area.width(), height, Qt.AlignCenter, number)
            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    def line_number_area_width(self):
        digits = 4
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_margin(0)

    def update_line_number_area_margin(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def highlight_current_line(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor(233, 233, 233)
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
            self.setExtraSelections(extraSelections)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
            event.accept()
        else:
            super().wheelEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_F and (event.modifiers() & Qt.ControlModifier):
            self.find_key()
        elif event.key() == Qt.Key_Equal and (event.modifiers() & Qt.ControlModifier):
            self.zoom_in()
        elif event.key() == Qt.Key_Minus and (event.modifiers() & Qt.ControlModifier):
            self.zoom_out()
        elif event.key() == Qt.Key_Slash and (event.modifiers() & Qt.ControlModifier):
            self.toggle_comment()
        elif event.key() == Qt.Key_Z and (event.modifiers() & Qt.ControlModifier):
            super().keyPressEvent(event)
        elif event.key() == Qt.Key_Escape:
            if self.search_text_box is not None:
                self.search_text_box.hide()
                self.search_text_box = None
                self.clear_format()
        elif self.search_text_box is not None:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.next_pattern()
                event.ignore()
            else:
                super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def toggle_comment(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.StartOfBlock)
        cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
        selected_text = cursor.selectedText()
        if selected_text.lstrip().startswith("--"):
            txt_after_comment = selected_text.lstrip()[2:]
        else:
            txt_after_comment = "--" + selected_text.lstrip()
        cursor.beginEditBlock()
        cursor.removeSelectedText()
        cursor.insertText(txt_after_comment)
        cursor.endEditBlock()

    def find_key(self):
        if self.search_text_box is None:
            self.search_text_box = QLineEdit(self)
            position = self.geometry().topRight() - self.search_text_box.geometry().topRight() - QPoint(50, 0)
            self.search_text_box.move(position)
            self.search_text_box.show()
            self.search_text_box.textChanged.connect(self.find_with_pattern)
        self.search_text_box.setFocus()

    def find_with_pattern(self, pattern):
        self.setUndoRedoEnabled(False)
        self.clear_format()
        if pattern == "":
            return
        cursor = self.textCursor()
        regex = QRegExp(pattern)
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        self.current_index = index
        while index != -1:
            cursor.setPosition(index)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            cursor.mergeCharFormat(self.find_highlight_format)
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)
        if self.current_index != -1:
            cursor.setPosition(self.current_index)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            self.setTextCursor(cursor)
        self.setUndoRedoEnabled(True)
        self.current_pattern = pattern

    def next_pattern(self):
        self.setUndoRedoEnabled(False)
        if self.current_index == -1 and self.current_pattern is not None:
            return
        cursor = self.textCursor()
        regex = QRegExp(self.current_pattern)
        pos = self.current_index + regex.matchedLength()
        self.current_index = regex.indexIn(self.toPlainText(), pos)
        pos = self.current_index + regex.matchedLength()
        self.current_index = regex.indexIn(self.toPlainText(), pos)
        if self.current_index != -1:
            cursor.setPosition(self.current_index)
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor, 1)
            self.setTextCursor(cursor)
        else:
            self.current_index = regex.indexIn(self.toPlainText(), 0)
            cursor.setPosition(self.current_index)
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
        self.current_index = -1
        self.current_pattern = None

    def zoom_in(self):
        self.zoomIn(1)

    def zoom_out(self):
        self.zoomOut(1)
