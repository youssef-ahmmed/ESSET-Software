class SpiProtocolDTO:
    def __init__(self, significant_bit, clk_state, clk_phase, data_size):
        self.significant_bit = significant_bit
        self.clk_state = clk_state
        self.clk_phase = clk_phase
        self.data_size = data_size
