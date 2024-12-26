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
from networksecurity.entity.artifact import (TrainingPipelineArtifact,DataIngestionArtifact, DataTransformationArtifact,
                                             DataValidationArtifact,ModelEvaluationArtifact,ModelRegistryArtifact,
                                             ModelTrainingArtifact)

import os
import sys


class TrainingPipeline:

    def __init__(self):
        pass

    # 1.
    def start_data_ingestion(self):
        try:
            pass
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
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])