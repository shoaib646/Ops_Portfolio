# import os
# import sys
#
# from networksecurity.exception.exception import NetworkSecurityException
# from networksecurity.logger.logger import logging
#
# from networksecurity.entity.artifact import DataTransformationArtifact, ModelTrainingArtifact
# from networksecurity.entity.config import ModelTrainingConfig
#
# from xgboost import XGBClassifier
# from sklearn.base import BaseEstimator, ClassifierMixin
# from sklearn.model_selection import GridSearchCV
#
# from networksecurity.utils.ML.model.estimator import NetworkModel
# from networksecurity.utils.Main.utils import save_object, load_object
# from networksecurity.utils.Main.utils import load_numpy_array_data
# from networksecurity.utils.ML.metric.classification_metric import get_classification_score
#
# class SklearnCompatibleXGBClassifier(XGBClassifier, BaseEstimator, ClassifierMixin):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def _more_tags(self):
#         return {'requires_positive_y': False}
#
# class ModelTraining:
#
#     def __init__(self, model_trainer_config: ModelTrainingConfig,
#                  LastArtifact: DataTransformationArtifact):
#         try:
#             self.model_trainer_config = model_trainer_config
#             self.data_transformation_artifact = LastArtifact
#         except Exception as e:
#             raise NetworkSecurityException(e, sys)
#
#     def perform_hyper_parameter_tuning(self, x_train, y_train):
#         """
#         Perform hyperparameter tuning using GridSearchCV.
#         """
#         try:
#             # Define hyperparameter grid
#             param_grid = {
#                 'n_estimators': [100, 200, 300],
#                 'max_depth': [3, 5, 7],
#                 'learning_rate': [0.01, 0.1, 0.2],
#                 'subsample': [0.8, 1.0],
#                 'colsample_bytree': [0.8, 1.0],
#             }
#
#             xgb_clf = SklearnCompatibleXGBClassifier()
#
#             grid_search = GridSearchCV(estimator=xgb_clf,
#                                        param_grid=param_grid,
#                                        scoring='f1',
#                                        cv=3,
#                                        verbose=1,
#                                        n_jobs=-1)
#
#             grid_search.fit(x_train, y_train)
#
#             # Return the best model
#             best_model = grid_search.best_estimator_
#             logging.info(f"Best hyperparameters: {grid_search.best_params_}")
#             return best_model
#         except Exception as e:
#             raise NetworkSecurityException(e, sys)
#
#     def train_model(self, x_train, y_train):
#         try:
#             tuned_model = self.perform_hyper_parameter_tuning(x_train, y_train)
#             return tuned_model
#         except Exception as e:
#             raise e
#
#     def initiate_training(self) -> ModelTrainingArtifact:
#         try:
#             train_file_path = self.data_transformation_artifact.transformed_train_filepath
#             test_file_path = self.data_transformation_artifact.transformed_test_filepath
#
#             # loading training array and testing array
#             train_arr = load_numpy_array_data(train_file_path)
#             test_arr = load_numpy_array_data(test_file_path)
#
#             x_train, y_train, x_test, y_test = (
#                 train_arr[:, :-1],
#                 train_arr[:, -1],
#                 test_arr[:, :-1],
#                 test_arr[:, -1],
#             )
#
#             model = self.train_model(x_train, y_train)
#             y_train_pred = model.predict(x_train)
#             classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)
#
#             if classification_train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
#                 raise Exception("Trained model is not good to provide expected accuracy")
#
#             y_test_pred = model.predict(x_test)
#             classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)
#
#             # Overfitting and Underfitting
#             diff = abs(classification_train_metric.f1_score - classification_test_metric.f1_score)
#
#             if diff > self.model_trainer_config.overfitting_underfitting_threshold:
#                 raise Exception("Model is not good try to do more experimentation.")
#
#             preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_filepath)
#
#             model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
#             os.makedirs(model_dir_path, exist_ok=True)
#             Network_Model = NetworkModel(preprocessor=preprocessor, model=model)
#             save_object(self.model_trainer_config.trained_model_file_path, obj=Network_Model)
#
#             # model trainer artifact
#
#             model_trainer_artifact = ModelTrainingArtifact(
#                 trained_model_file_path=self.model_trainer_config.trained_model_file_path,
#                 train_metric_artifact=classification_train_metric,
#                 test_metric_artifact=classification_test_metric)
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")
#             return model_trainer_artifact
#         except Exception as e:
#             raise NetworkSecurityException(e, sys)


import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from sklearn.model_selection import RandomizedSearchCV

from networksecurity.entity.artifact import DataTransformationArtifact, ModelTrainingArtifact
from networksecurity.entity.config import ModelTrainingConfig

from xgboost import XGBClassifier
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import GridSearchCV

from networksecurity.utils.ML.model.estimator import NetworkModel
from networksecurity.utils.Main.utils import save_object, load_object
from networksecurity.utils.Main.utils import load_numpy_array_data
from networksecurity.utils.ML.metric.classification_metric import get_classification_score

class SklearnCompatibleXGBClassifier(XGBClassifier, BaseEstimator, ClassifierMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __sklearn_tags__(self):
        tags = {
            'requires_positive_y': False,
            'non_deterministic': False
        }
        return tags

class ModelTraining:

    def __init__(self, model_trainer_config: ModelTrainingConfig,
                 LastArtifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = LastArtifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # def perform_hyper_parameter_tuning(self, x_train, y_train):
    #     """
    #     Perform hyperparameter tuning using RandomizedSearchCV.
    #     """
    #     try:
    #         param_dist = {
    #             'n_estimators': [100, 200, 300],
    #             'max_depth': [3, 5, 7],
    #             'learning_rate': [0.01, 0.1, 0.2],
    #             'subsample': [0.8, 1.0],
    #             'colsample_bytree': [0.8, 1.0],
    #         }
    #
    #         xgb_clf = XGBClassifier()
    #
    #         random_search = RandomizedSearchCV(
    #             estimator=xgb_clf,
    #             param_distributions=param_dist,
    #             scoring='f1',
    #             n_iter=50,
    #             cv=3,
    #             verbose=1,
    #             n_jobs=-1,
    #             random_state=42
    #         )
    #
    #         random_search.fit(x_train, y_train)
    #
    #         best_model = random_search.best_estimator_
    #         logging.info(f"Best hyperparameters: {random_search.best_params_}")
    #         return best_model
    #     except Exception as e:
    #         raise NetworkSecurityException(e, sys)

    def train_model(self, x_train, y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x_train, y_train)
            return xgb_clf
        except Exception as e:
            raise e

    def initiate_training(self) -> ModelTrainingArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_filepath
            test_file_path = self.data_transformation_artifact.transformed_test_filepath

            # loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )

            model = self.train_model(x_train, y_train)
            y_train_pred = model.predict(x_train)
            classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)

            if classification_train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
                raise Exception("Trained model is not good to provide expected accuracy")

            y_test_pred = model.predict(x_test)
            classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            # Overfitting and Underfitting
            diff = abs(classification_train_metric.f1_score - classification_test_metric.f1_score)

            if diff > self.model_trainer_config.overfitting_underfitting_threshold:
                raise Exception("Model is not good try to do more experimentation.")

            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_filepath)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path, exist_ok=True)
            Network_Model = NetworkModel(preprocessor=preprocessor, model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=Network_Model)

            # model trainer artifact

            model_trainer_artifact = ModelTrainingArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric_artifact=classification_train_metric,
                test_metric_artifact=classification_test_metric)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
