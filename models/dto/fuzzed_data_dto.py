class FuzzedDataDto:
    def __init__(self, message: str, message_length: int, message_entropy: float,
                 response: str, response_length: int, response_entropy: float):
        self.message = message
        self.message_length = message_length
        self.message_entropy = message_entropy
        self.response = response
        self.response_length = response_length
        self.response_entropy = response_entropy
