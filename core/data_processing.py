
class DataProcessing:
    def __init__(self, data):
        self.data = data
        self.fuzzed_string_data = None
        self.fuzzed_hex_data = None

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

    def combine_fuzzed_data_to_string(self):
        if self.fuzzed_string_data:
            return self.fuzzed_string_data

        combined_data = []
        for item in self.data:
            if isinstance(item, list):
                combined_data.append(''.join(map(str, item)))
            else:
                combined_data.append(item)
        
        self.fuzzed_string_data = ''.join(combined_data)
        return self.fuzzed_string_data

    def combine_fuzzed_data_to_hex_string(self):
        if self.fuzzed_hex_data:
            return self.fuzzed_hex_data

        self.fuzzed_hex_data = ""
        for item in self.data:
            if isinstance(item, list):
                item_hex = ''.join([f"0x{byte:02X}" for byte in item])
                self.fuzzed_hex_data += '\\' + item_hex
            else:
                item_hex = ''.join([f"0x{byte:02X}" for byte in item.encode()])
                self.fuzzed_hex_data += '\\' + item_hex

        return self.fuzzed_hex_data

    def combine_fuzzed_data_to_hex_list(self):
        hex_list = []
        for item in self.data:
            if isinstance(item, list):
                hex_list.append(''.join([f"0x{byte:02X}" for byte in item]))
            else:
                hex_list.append(''.join([f"0x{byte:02X}" for byte in item.encode()]))

        return hex_list
