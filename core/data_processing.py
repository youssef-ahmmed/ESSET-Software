
class DataProcessing:
    def __init__(self, data):
        self.data = data

    def convert_data_to_decimal(self):
        return [int(byte) for byte in self.data]

    def convert_decimal_to_binary(self):
        decimal_data = self.convert_data_to_decimal()
        return [(bin(byte)[2:].zfill(8)) for byte in decimal_data]

    def convert_decimal_to_hex(self):
        decimal_data = self.convert_data_to_decimal()
        return [f'/x{hex(byte)[2:].zfill(2).upper()}' for byte in decimal_data]
