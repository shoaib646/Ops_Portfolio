from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.constant import  variables
from networksecurity.utils.Main.utils import read_yaml_file,write_yaml_file
from networksecurity.constant.variables import SCHEMA_FILE
import  pandas as pd

import pickle


from networksecurity.components.DataIngestion import DataIngestion
from networksecurity.components.DataTransformation import DataTransformation
from networksecurity.components.DataValidation import DataValidation
from networksecurity.components.ModelEvaluation import ModelEvaluation
from networksecurity.components.ModelRegistry import ModelRegistry
from networksecurity.components.ModelTraining import ModelTraining

from networksecurity.entity.config import (TrainingPipelineConfig,DataIngestionConfig, DataTransformationConfig,
                                           DataValidationConfig,ModelEvaluationConfig,ModelRegistryConfig,
                                           ModelTrainingConfig)
from networksecurity.entity.artifact import (DataIngestionArtifact, DataTransformationArtifact,
                                             DataValidationArtifact,ModelEvaluationArtifact,ModelRegistryArtifact,
                                             ModelTrainingArtifact)

import os
import sys


class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = None
        self.training_pipeline_config = TrainingPipelineConfig()
        self.__scehma_config = read_yaml_file(SCHEMA_FILE)

    # 1.
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion...")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            # Save the artifact for future runs
            artifact_path = os.path.join(variables.ARTIFACT_DIR, variables.IngestionArtifactPath)
            os.makedirs(os.path.dirname(artifact_path), exist_ok=True)
            with open(artifact_path, "wb") as file:
                pickle.dump(data_ingestion_artifact, file)

            logging.info(f"Data ingestion completed. Artifact saved at {artifact_path}.")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    # 2
    def start_data_validation(self, LastArtifact: DataIngestionArtifact) -> 'DataValidationArtifact':
        try:
            logging.info("Starting data validation...")
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_validation_config=data_validation_config, LastArtifact=LastArtifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Data validation completed.")
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # 3.
    def start_data_transformation(self, LastArtifact: DataValidationArtifact) -> 'DataTransformationArtifact':
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_transformation_config= data_transformation_config, LastArtifact=LastArtifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()

            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 4.
    def model_trainer(self, LastArtifact:DataTransformationArtifact) -> 'ModelTrainingArtifact':
        try:
            model_trainer_config = ModelTrainingConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTraining(model_trainer_config=model_trainer_config, LastArtifact=LastArtifact)

            model_trainer_artifact = model_trainer.initiate_training()
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 5.
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 6.
    def start_model_registry(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])


    def run_pipeline(self):

        try:
            # Initialize variables
            data_ingestion_artifact = None  # Proper initialization
            data_validation_artifact = None
            ingestion_artifact_path = os.path.join(variables.ARTIFACT_DIR, variables.IngestionArtifactPath)

            # Schema expectations
            expected_numerical_cols = len(self.__scehma_config["numerical_columns"])
            expected_total_columns = len(self.__scehma_config["columns"])

            # Check for existing ingestion artifact
            if os.path.exists(ingestion_artifact_path):
                logging.info("Loading existing data ingestion artifact...")
                with open(ingestion_artifact_path, "rb") as file:
                    data_ingestion_artifact = pickle.load(file)

                # Validate train and test files against schema
                train_file, test_file = data_ingestion_artifact.trained_file_path, data_ingestion_artifact.test_file_path
                train_columns = pd.read_csv(train_file).shape[1]
                test_columns = pd.read_csv(test_file).shape[1]

                if train_columns == expected_total_columns and test_columns == expected_total_columns:
                    logging.info("Total columns in train and test data match the schema.")

                    train_numerical_columns = pd.read_csv(train_file).select_dtypes(include="number").shape[1]
                    test_numerical_columns = pd.read_csv(test_file).select_dtypes(include="number").shape[1]

                    if train_numerical_columns == expected_numerical_cols and test_numerical_columns == expected_numerical_cols:
                        logging.info("Numerical columns in train and test data match the schema.")
                        logging.info("Existing data ingestion artifact matches the schema.")
                    else:
                        logging.warning("Numerical columns do not match the schema. Re-running data ingestion.")
                        data_ingestion_artifact = self.start_data_ingestion()
                else:
                    logging.warning("Total columns do not match the schema. Connecting MongoDB for data ingestion.")
                    data_ingestion_artifact = self.start_data_ingestion()
            else:
                logging.info("No existing artifact found. Starting data ingestion...")
                data_ingestion_artifact = self.start_data_ingestion()

            # Proceed to data validation
            if data_ingestion_artifact:
                data_validation_artifact = self.start_data_validation(LastArtifact=data_ingestion_artifact)
                logging.info("Data Validation completed successfully.")
            else:
                raise ValueError("Data Ingestion artifact is invalid or missing.")


            # Proceed to data Transformation
            if data_validation_artifact:
                data_transformation_artifact = self.start_data_transformation(LastArtifact=data_validation_artifact)
                logging.info("Data Transformation completed successfully.")
            else:
                raise ValueError("Data Validation artifact is invalid or missing.")

            if data_transformation_artifact:
                model_trainer_artifact = self.model_trainer(LastArtifact=data_transformation_artifact)
                logging.info("Model Training completed successfully.")
            else:
                raise ValueError("Data Transformation artifact is invalid or missing.")


        except Exception as e:
            logging.error(f"Error in running the pipeline: {str(e)}")
            raise NetworkSecurityException(e, sys)
