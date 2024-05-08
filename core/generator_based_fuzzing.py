import random
import string


class GeneratorBasedFuzzing:
    __fuzzed_data = None

    def __init__(self, number_of_messages: int, bytes_per_message: int):
        self.number_of_messages = number_of_messages
        self.bytes_per_message = bytes_per_message

    @classmethod
    def get_fuzzed_data(cls):
        return cls.__fuzzed_data

    @classmethod
    def set_fuzzed_data(cls, value=None):
        cls.__fuzzed_data = value

    def generate_random_data_by_type(self, data_type):
        get_random_data_by_datatype = {
            "Number": self.generate_number_data,
            "String": self.generate_string_data,
            "Mixed": self.generate_mixed_data
        }

        return get_random_data_by_datatype.get(data_type)()

    def generate_number_data(self):
        self.__class__.set_fuzzed_data([[random.randint(0, 255) for _ in range(self.bytes_per_message)]
                                        for _ in range(self.number_of_messages)])

    def generate_string_data(self):
        self.__class__.set_fuzzed_data([''.join(random.choices(string.ascii_letters, k=self.bytes_per_message)) for _ in
                                        range(self.number_of_messages)])

    def generate_mixed_data(self):
        self.__class__.set_fuzzed_data([])
        for _ in range(self.number_of_messages):
            if random.random() < 0.5:
                self.__class__.get_fuzzed_data().append([random.randint(0, 255) for _ in range(self.bytes_per_message)])
            else:
                self.__class__.get_fuzzed_data().append(''.join(random.choices(string.ascii_letters + string.digits,
                                                                               k=self.bytes_per_message)))
