from PyQt5.QtCore import QRegularExpression, Qt
from PyQt5.QtGui import QFont, QTextCharFormat, QSyntaxHighlighter


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.highlighting_rules = []

        red_reserved_keyword_format = QTextCharFormat()
        red_reserved_keyword_format.setForeground(Qt.darkRed)
        red_reserved_keyword_format.setFontWeight(QFont.Bold)

        blue_reserved_keyword_format = QTextCharFormat()
        blue_reserved_keyword_format.setForeground(Qt.darkBlue)
        blue_reserved_keyword_format.setFontWeight(QFont.Bold)

        red_reserved_keyword_patterns = [
            r'\b(?:library|use|entity|architecture|is|begin|end|process|if|endif|then|else|elsif|'
            r'for|generate|component|port|in|out|buffer|map|and|or|not|xnor|xor|variable|when|while'
            r'with|case|end case|end process|of|all|generic|signal|downto|upto|:=|=>|<=|&|\||!)\b'
        ]

        blue_reserved_keyword_patterns = [
            r'\b(?::)?(?:positive|negative|rising_edge|falling_edge|std_logic|std_logic_vector|integer|'
            r'bit|but_vector|real|time|character|boolean|string|file|type|range|array|record|subtype'
            r'others|ieee)(?::)?\b'
        ]

        for pattern in red_reserved_keyword_patterns:
            self.highlighting_rules.append((QRegularExpression(pattern), red_reserved_keyword_format))

        for pattern in blue_reserved_keyword_patterns:
            self.highlighting_rules.append((QRegularExpression(pattern), blue_reserved_keyword_format))

        integer_format = QTextCharFormat()
        integer_format.setFontWeight(QFont.Bold)
        integer_format.setForeground(Qt.blue)
        self.highlighting_rules.append((QRegularExpression(r'(?<!_)\b-?\d+\b'), integer_format))

        self.comment_start_expression = QRegularExpression(r'/\*')
        self.comment_end_expression = QRegularExpression(r'\*/')

        single_line_comment_format = QTextCharFormat()
        single_line_comment_format.setForeground(Qt.darkGreen)
        self.highlighting_rules.append((QRegularExpression(r'--.*'), single_line_comment_format))

        self.multi_line_comment_format = QTextCharFormat()
        self.multi_line_comment_format.setForeground(Qt.darkGreen)
        self.comment_start_expression = QRegularExpression(r'/\*')
        self.comment_end_expression = QRegularExpression(r'\*/')
        self.highlighting_rules.append((self.comment_start_expression, self.multi_line_comment_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != 1:
            match = self.comment_start_expression.match(text)
            start_index = match.capturedStart() if match.hasMatch() else -1

        while start_index >= 0:
            match = self.comment_end_expression.match(text, start_index)
            end_index = match.capturedStart()
            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
            else:
                comment_length = end_index - start_index + match.capturedLength()
            self.setFormat(start_index, comment_length, self.multi_line_comment_format)
            match = self.comment_start_expression.match(text, start_index + comment_length)
            start_index = match.capturedStart() if match.hasMatch() else -1
