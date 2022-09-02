from deepClassifier.utils import get_size
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from tqdm import tqdm
import os
from zipfile import ZipFile
import urllib.request as request


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def sample_method(self):
        pass