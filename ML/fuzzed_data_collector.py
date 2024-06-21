import json
import csv

from ML.model_preprocessing import ModelPreprocessing
from controllers.project_path_controller import ProjectPathController
from models.dao.fuzzed_data_dao import FuzzedDataDao
from reusable_functions.os_operations import join_paths


class FuzzedDataCollector:
    def __init__(self):
        self.project_path = ProjectPathController.get_instance().get_project_path()

    def construct_message_response_table(self):
        fuzzed_data_list = []
        for message, response in self.get_message_response_data().items():
            fuzzed_data_list.append({
                    "message": message,
                    "message_length": len(message.split('0x')[1:]),
                    "message_entropy": ModelPreprocessing.entropy(message),
                    "response": response,
                    "response_length": len(response.split('0x')[1:]),
                    "response_entropy": ModelPreprocessing.entropy(response)
            })

        return fuzzed_data_list

    def get_message_response_data(self):
        json_path = join_paths(self.project_path, "MessageResponseFuzzing.json")
        with open(json_path, 'r') as file:
            message_response_data = json.load(file)

        return message_response_data

    def write_data_to_csv(self):
        csv_file_path = join_paths(self.project_path, "output.csv")
        data = FuzzedDataDao.get_all()
        headers = ['message', 'message_length', 'message_entropy', 'response', 'response_length', 'response_entropy']

        with open(csv_file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(headers)
            for row in data:
                csv_writer.writerow([
                    row.message,
                    row.message_length,
                    row.message_entropy,
                    row.response,
                    row.response_length,
                    row.response_entropy
                ])
