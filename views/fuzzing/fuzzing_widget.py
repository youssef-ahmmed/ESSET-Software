from PyQt5.QtWidgets import QWidget, QHBoxLayout

from views.fuzzing.data_preparation_widget import DataPreparationWidget


class FuzzingWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.data_preparation_widget = DataPreparationWidget()
        self.create_layout()

    def create_layout(self):
        widgets_layout = QHBoxLayout()
        widgets_layout.addWidget(self.data_preparation_widget)

        self.setLayout(widgets_layout)
