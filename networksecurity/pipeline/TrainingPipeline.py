from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


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

    # 1.
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 2.
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 3.
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    # 4.
    def model_trainer(self):
        try:
            pass
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

    # main.
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])