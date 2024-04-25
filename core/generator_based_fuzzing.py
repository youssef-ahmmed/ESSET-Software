import random
import string


class GeneratorBasedFuzzing:

    def __init__(self, number_of_messages: int, bytes_per_message: int):
        self.number_of_messages = number_of_messages
        self.bytes_per_message = bytes_per_message
        self.get_random_data_by_datatype = {
            "Number": self.generate_number_data,
            "String": self.generate_string_data,
            "Mixed": self.generate_mixed_data
        }

    def get_random_data_by_type(self, data_type):
        return self.get_random_data_by_datatype.get(data_type)()

    def generate_number_data(self):
        return [[random.randint(0, 255) for _ in range(self.bytes_per_message)]
                for _ in range(self.number_of_messages)]

    def generate_string_data(self):
        return [''.join(random.choices(string.ascii_letters, k=self.bytes_per_message)) for _ in
                range(self.number_of_messages)]

    def generate_mixed_data(self):
        result = []
        for _ in range(self.number_of_messages):
            if random.random() < 0.5:
                result.append([random.randint(0, 255) for _ in range(self.bytes_per_message)])
            else:
                result.append(''.join(random.choices(string.ascii_letters + string.digits, k=self.bytes_per_message)))
        return result
