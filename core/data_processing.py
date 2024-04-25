
class DataProcessing:
    def __init__(self, data):
        self.data = data

    def convert_data_to_decimal(self):
        return [int(byte) for byte in self.data]

    def convert_decimal_to_binary(self):
        decimal_data = self.convert_data_to_decimal()
        return [(bin(byte)[2:].zfill(8)) for byte in decimal_data]

    def convert_byte_list_to_bit_list(self):
        byte_list = self.convert_decimal_to_binary()
        return [int(bit) for byte in byte_list for bit in byte]

    def convert_decimal_to_hex(self):
        decimal_data = self.convert_data_to_decimal()
        return [f'/x{hex(byte)[2:].zfill(2).upper()}' for byte in decimal_data]

    def combine_data_to_string(self):
        combined_data = []
        for item in self.data:
            if isinstance(item, list):
                combined_data.append(''.join(map(str, item)))
            else:
                combined_data.append(item)
        return ''.join(combined_data)

    def combine_data_to_hex(self):
        combined_hex = ""
        for item in self.data:
            if isinstance(item, list):
                item_hex = ''.join([f"0x{byte:02X}" for byte in item])
                combined_hex += '\\' + item_hex
            else:
                item_hex = ''.join([f"0x{byte:02X}" for byte in item.encode()])
                combined_hex += '\\' + item_hex
        return combined_hex
