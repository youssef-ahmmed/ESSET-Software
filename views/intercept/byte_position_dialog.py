from qfluentwidgets import MessageBoxBase, SubtitleLabel, ComboBox


class BytePositionDialog(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Select Byte Position You Want To Flip: ', self)
        self.positions = ComboBox()

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.positions)

        self.yesButton.setText('yes')
        self.cancelButton.setText('no')

        self.widget.setMinimumWidth(350)

    def get_selected_byte(self):
        return self.positions.currentText()
