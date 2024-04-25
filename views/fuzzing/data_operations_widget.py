from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from qfluentwidgets import ComboBox, LineEdit


class DataOperationsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.protocol_list = ['Choose', 'UART', 'SPI']

        self.initialize_widget()
        self.create_layout()

    def initialize_widget(self):
        self.create_labels()
        self.create_comboboxes()
        self.comboboxes_size()
        self.create_lineedits()

    def create_labels(self):
        self.data_type_label = QLabel('Data Type:')
        self.number_bytes_label = QLabel('Number of bytes per message:')
        self.number_messages_label = QLabel('Number of messages:')
        self.fuzzing_protocol_label = QLabel('Fuzzing on:')
        self.sniffing_protocol_label = QLabel('Sniffing on:')

    def create_comboboxes(self):
        self.data_types_combobox = ComboBox()
        self.data_types_combobox.addItems(['Choose', 'Number', 'String', 'Mixed'])

        self.fuzzing_protocols_combobox = ComboBox()
        self.fuzzing_protocols_combobox.addItems(self.protocol_list)

        self.sniffing_protocols_combobox = ComboBox()
        self.sniffing_protocols_combobox.addItems(self.protocol_list)

    def comboboxes_size(self):
        self.data_types_combobox.setMinimumWidth(675)
        self.fuzzing_protocols_combobox.setMinimumWidth(210)
        self.sniffing_protocols_combobox.setMinimumWidth(250)

    def create_lineedits(self):
        self.number_bytes_input = LineEdit()
        self.number_bytes_input.setPlaceholderText("Enter the number of bytes per message...")
        self.number_messages_input = LineEdit()
        self.number_messages_input.setPlaceholderText("Enter the number of messages...")

        self.number_messages_input.setValidator(QIntValidator())
        self.number_bytes_input.setValidator(QIntValidator())

    def create_layout(self):
        main_layout = QVBoxLayout()

        data_type_layout = QHBoxLayout()
        data_type_layout.addWidget(self.data_type_label)
        data_type_layout.addWidget(self.data_types_combobox)
        main_layout.addLayout(data_type_layout)

        messages_number_layout = QHBoxLayout()
        messages_number_layout.addWidget(self.number_messages_label)
        messages_number_layout.addWidget(self.number_messages_input)
        main_layout.addLayout(messages_number_layout)

        bytes_number_layout = QHBoxLayout()
        bytes_number_layout.addWidget(self.number_bytes_label)
        bytes_number_layout.addWidget(self.number_bytes_input)
        main_layout.addLayout(bytes_number_layout)

        protocol_layout = QHBoxLayout()
        protocol_layout.addWidget(self.fuzzing_protocol_label)
        protocol_layout.addWidget(self.fuzzing_protocols_combobox)

        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        protocol_layout.addSpacerItem(spacer)

        protocol_layout.addWidget(self.sniffing_protocol_label)
        protocol_layout.addWidget(self.sniffing_protocols_combobox)
        main_layout.addLayout(protocol_layout)

        self.setLayout(main_layout)

    def get_selected_fuzzing_protocol(self):
        return self.fuzzing_protocols_combobox.text()

    def get_selected_sniffing_protocol(self):
        return self.sniffing_protocols_combobox.text()

    def get_selected_data_type(self):
        return self.data_types_combobox.text()

    def get_number_bytes_input(self):
        return self.number_bytes_input.text()

    def get_number_of_messages(self):
        return self.number_messages_input.text()
