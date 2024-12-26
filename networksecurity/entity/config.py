from datetime import datetime
import os
from networksecurity.constant import variables



class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")):
        self.pipeline_name = variables.PIPELINE_NAME
        self.artifact_name = variables.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp




class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, variables.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, variables.DATA_INGESTION_FEATURE_STORE_DIR, variables.FILENAME
        )
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, variables.DATA_INGESTION_INGESTED_DIR, variables.TRAIN_FILE
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir, variables.DATA_INGESTION_INGESTED_DIR, variables.TEST_FILE
        )
        self.train_test_split_ratio: float = variables.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = variables.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = variables.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    def __init__(self):
        pass

class DataTransformationConfig:
    def __init__(self):
        pass

class ModelTrainingConfig:
    def __init__(self):
        pass

class ModelEvaluationConfig:
    def __init__(self):
        pass

class ModelRegistryConfig:
    def __init__(self):
        pass

