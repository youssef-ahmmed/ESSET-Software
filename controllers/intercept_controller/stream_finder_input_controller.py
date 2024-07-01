from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


class StreamFinderInputController(QObject):
    _instance = None

    @staticmethod
    def get_instance(stream_finder_input=None):
        if StreamFinderInputController._instance is None:
            StreamFinderInputController._instance = StreamFinderInputController(stream_finder_input)
        return StreamFinderInputController._instance

    def __init__(self, stream_finder_input):
        super(StreamFinderInputController, self).__init__()

        if StreamFinderInputController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.stream_finder_input = stream_finder_input

    def get_input_stream(self):
        return ''.join(format(ord(c), '02x') for c in self.stream_finder_input.text())

    def get_input_stream_size(self):
        text_input = self.stream_finder_input.text()
        return len(text_input.encode('utf-8'))*8
