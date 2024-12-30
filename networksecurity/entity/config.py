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
    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> None:

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
    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> None:

        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                     variables.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, variables.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir,
                                                  variables.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, variables.TRAIN_FILE)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, variables.TEST_FILE)
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, variables.TRAIN_FILE)
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, variables.TEST_FILE)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            variables.DATA_VALIDATION_DRIFT_REPORT_DIR,
            variables.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        pass

class ModelTrainingConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        pass

class ModelEvaluationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        pass

class ModelRegistryConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        pass

