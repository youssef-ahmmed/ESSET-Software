from qfluentwidgets import MessageBoxBase, SubtitleLabel, ComboBox


class BitPositionDialog(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Select Byte Position You Want To Flip: ', self)
        self.positions = ComboBox()

        self.byte_positions = ['0', '1', '2', '3', '4', '5', '6', '7']

        self.positions.addItems(self.byte_positions)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.positions)

        self.yesButton.setText('yes')
        self.cancelButton.setText('no')

        self.widget.setMinimumWidth(350)

    def update_positions_combobox(self, data):
        self.byte_positions.clear()

        num_bytes = len(data) // 4

        for i in range(num_bytes):
            self.byte_positions.append(str(i))

        self.positions.addItems(self.byte_positions)
