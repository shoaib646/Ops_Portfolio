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
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                         variables.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir,
                                                             variables.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                             variables.TRAIN_FILE.replace("csv","npy"), )
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,
                                                            variables.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                            variables.TEST_FILE.replace("csv","npy"), )
        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir,
                                                              variables.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                              variables.PREPROCESS_FILE)


class ModelTrainingConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, variables.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir, variables.MODEL_TRAINER_TRAINED_MODEL_DIR,
            variables.MODEL_FILE
        )
        self.expected_accuracy: float = variables.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = variables.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD

class ModelEvaluationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_evaluation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, variables.MODEL_EVALUATION_DIR_NAME
        )
        self.report_file_path = os.path.join(self.model_evaluation_dir,
                                             variables.MODEL_EVALUATION_REPORT_NAME)
        self.change_threshold = variables.MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE

class ModelRegistryConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_evaluation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, variables.MODEL_PUSHER_DIR_NAME
        )
        self.model_file_path = os.path.join(self.model_evaluation_dir, variables.MODEL_FILE)
        timestamp = round(datetime.now().timestamp())
        self.saved_model_path = os.path.join(
            variables.SAVED_MODEL_DIR,
            f"{timestamp}",
            variables.MODEL_FILE)

