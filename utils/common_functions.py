import os
import sys
from src.logger import logging
from src.custom_exception import CustomException
import yaml
import pandas as pd

def read_yaml(file_path: str):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")    
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            return config
    except FileNotFoundError as e:
        logging.error(f"Error reading YAML file: {e}")
        raise CustomException(e, sys)
    

def load_data(path):
    try:
        logging.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)





