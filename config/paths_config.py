import os

## Data Ingestion ##
ARTIFACTS_DIR = "artifacts"
RAW_DIR = os.path.join(ARTIFACTS_DIR,"raw")
RAW_FILE_PATH = os.path.join(RAW_DIR,"raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR,"train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR,"test.csv")

CONFIG_PATH = "config/config.yaml"

