import os
import sys
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import socket

from google.auth.environment_vars import AWS_ACCESS_KEY_ID

from networksecurity.entity.artifact import DataIngestionArtifact

load_dotenv()


# Common variables
TARGET_COL = "Result"
PIPELINE_NAME = "SecuredURLs"
ARTIFACT_DIR:str= 'Artifacts'
FILENAME:str="NetworkDataFormed.csv"

IngestionArtifactPath = "data_ingestion_artifact.pkl"


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

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "driftreport.yaml"



# Data Transformation Variables
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"

# Data Trainer Variables
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

# Data Evaluation Variables

MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_REPORT_NAME= "report.yaml"


MODEL_PUSHER_DIR_NAME = "model_registry"
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR

TRAINING_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
PREDICTION_BUCKET_NAME = "my-url-datasource"


HOSTNAME = socket.gethostbyname(socket.gethostname())
PORT = 8000

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
