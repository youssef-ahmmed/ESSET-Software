from qfluentwidgets import MessageBoxBase, SubtitleLabel, ComboBox


class BitPositionDialog(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Select Bit Position You Want To Flip: ', self)
        self.positions = ComboBox()

        self.bits_positions = ['0', '1', '2', '3', '4', '5', '6', '7']

        self.positions.addItems(self.bits_positions)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.positions)

        self.yesButton.setText('yes')
        self.cancelButton.setText('no')

        self.widget.setMinimumWidth(350)
