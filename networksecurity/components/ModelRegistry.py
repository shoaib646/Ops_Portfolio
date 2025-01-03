from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.entity.artifact import ModelRegistryArtifact, ModelTrainingArtifact, ModelEvaluationArtifact
from networksecurity.entity.config import ModelEvaluationConfig, ModelRegistryConfig
import os, sys
from networksecurity.utils.ML.metric.classification_metric import get_classification_score
from networksecurity.utils.Main.utils import save_object, load_object, write_yaml_file
import shutil


class ModelRegister:

    def __init__(self, ModelRegisterConfig, LastArtifact: ModelEvaluationArtifact):

        try:
            self.model_registry_config = ModelRegisterConfig
            self.model_eval_artifact = LastArtifact
        except  Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_register(self, ) -> ModelRegistryArtifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_file_path

            # Creating model pusher dir to save model
            model_file_path = self.model_registry_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=model_file_path)

            # saved model dir
            saved_model_path = self.model_registry_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            # prepare artifact
            model_pusher_artifact = ModelRegistryArtifact(saved_model_path=saved_model_path,
                                                        model_file_path=model_file_path)
            return model_pusher_artifact
        except  Exception as e:
            raise NetworkSecurityException(e, sys)
