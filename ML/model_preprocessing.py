import math
from collections import Counter

from controllers.project_path_controller import ProjectPathController
from models import log_messages
from reusable_functions.os_operations import join_paths
import pandas as pd
from sklearn.cluster import DBSCAN

from views.common.info_bar import create_error_bar


class ModelPreprocessing:

    def __init__(self):
        self.project_path = ProjectPathController.get_instance().get_project_path()
        self.csv_file_path = join_paths(self.project_path, "output.csv")

        self.data = None
        self.sorted_data = None
        self.high_entropy_threshold = None
        self.low_entropy_threshold = None

    def built_model(self):
        self.load_data()
        self.clean_data()
        self.apply_dbscan()
        self.sort_by_entropy()
        self.set_entropy_thresholds()
        self.categorize_entropy()

    @staticmethod
    def entropy(data_bytes):
        counter = Counter(data_bytes)
        total = len(data_bytes)

        entropy = 0.0
        for count in counter.values():
            probability = count / total
            entropy -= probability * math.log2(probability)

        return entropy

    def load_data(self):
        try:
            self.data = pd.read_csv(self.csv_file_path)
        except FileNotFoundError as e:
            create_error_bar(log_messages.LOAD_DATA_NO_FILE)
            raise e
        except Exception as e:
            create_error_bar(log_messages.LOAD_DATA_ERROR)
            raise e

    def clean_data(self):
        self.data.dropna(subset=['response'], inplace=True)

    def apply_dbscan(self, eps=0.1, min_samples=2):
        response_entropies = self.data['response_entropy'].values.reshape(-1, 1)
        dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(response_entropies)
        self.data['cluster'] = dbscan.labels_
        self.data = self.data[self.data['cluster'] != -1]

    def sort_by_entropy(self):
        self.sorted_data = self.data.sort_values(by='response_entropy', ascending=False)

    def set_entropy_thresholds(self):
        self.high_entropy_threshold = self.sorted_data['response_entropy'].quantile(0.75)
        self.low_entropy_threshold = self.sorted_data['response_entropy'].quantile(0.25)

    def categorize_entropy(self):
        bins = [-float('inf'), self.low_entropy_threshold, self.high_entropy_threshold, float('inf')]
        labels = ['Low', 'Medium', 'High']
        self.sorted_data['entropy_category'] = pd.cut(self.sorted_data['response_entropy'], bins=bins, labels=labels)

    def get_results(self):
        return self.sorted_data[
            ['message', 'response', 'entropy_category']]
