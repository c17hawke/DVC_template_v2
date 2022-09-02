from deepClassifier.constants import *
from deepClassifier.entity import DataIngestionConfig
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier import logger
import os

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH, 
        secrets_filepath=SECRETS_FILE_PATH):
        self.config = read_yaml(path_to_yaml=config_filepath)
        self.params = read_yaml(path_to_yaml=params_filepath)
        self.secrets = read_yaml(path_to_yaml=secrets_filepath)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Update below
        logger.info("getting configuration for data ingestion")
        data_ingestion_config = DataIngestionConfig(
            kwarg_1="kwarg",
        )
        return data_ingestion_config
        """
        pass