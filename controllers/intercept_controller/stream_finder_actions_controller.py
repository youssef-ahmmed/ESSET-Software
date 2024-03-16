from PyQt5.QtCore import QObject

from models.log_messages import instance_exists_error


class StreamFinderActionsController(QObject):
    _instance = None

    @staticmethod
    def get_instance(stream_finder_action=None):
        if StreamFinderActionsController._instance is None:
            StreamFinderActionsController._instance = StreamFinderActionsController(stream_finder_action)
        return StreamFinderActionsController._instance

    def __init__(self, stream_finder_action):
        super(StreamFinderActionsController, self).__init__()

        if StreamFinderActionsController._instance is not None:
            raise Exception(instance_exists_error(self.__class__.__name__))

        self.stream_finder_action = stream_finder_action

    def get_selected_stream_finder_action(self):
        return self.stream_finder_action.currentText()
