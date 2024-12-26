import os
import sys
import numpy as np
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


# Common variables
TARGET_COL = "Result"
PIPELINE_NAME = "SecuredURLs"
ARTIFACT_DIR:str= 'Artifacts'
FILENAME:str="NetworkData.csv"

TRAIN_FILE:str= 'train.csv'
TEST_FILE:str= 'test.csv'

PREPROCESS_FILE:str= 'preprocessed.pkl'
MODEL_FILE:str= 'model.pkl'
SCHEMA_FILE:str= os.path.join("Schema","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"

SAVED_MODEL_DIR = os.path.join("saved_models")

# Data Ingestion Variables

DATA_INGESTION_COLLECTION_NAME: str = os.environ.get('COLLECTION_NAME')
DATA_INGESTION_DATABASE_NAME: str = os.environ.get('DB_NAME')
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2




# Data Transformation Variables

# Data Validation Variables

# Data Transformation Variables


# Data Trainer Variables

# Data Evaluation Variables