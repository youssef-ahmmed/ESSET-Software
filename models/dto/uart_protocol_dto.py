class UartProtocolDTO:
    def __init__(self, sniffed_data_id, clk_per_bit, baud_rate, data_size, stop_bit, parity_bit):
        self.sniffed_data_id = sniffed_data_id
        self.clk_per_bit = clk_per_bit
        self.baud_rate = baud_rate
        self.data_size = data_size
        self.stop_bit = stop_bit
        self.parity_bit = parity_bit
