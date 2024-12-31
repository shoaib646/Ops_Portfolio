from networksecurity.constant.variables import SCHEMA_FILE, DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
from networksecurity.entity.artifact import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.utils.Main.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os,sys, yaml



class DataValidation:

    def __init__(self, data_validation_config,LastArtifact:DataIngestionArtifact):
        try:
            self.data_ingestion_artifact = LastArtifact
            self.data_validation_config = data_validation_config
            self.__scehma_config = read_yaml_file(SCHEMA_FILE)
        except Exception as e:
            raise NetworkSecurityException(str(e))

    def validate_no_of_cols(self, dataframe:pd.DataFrame)-> bool:
        try:
            number_of_columns = len(self.__scehma_config["columns"])
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")

            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(str(e))

    def numerical_cols(self, dataframe: pd.DataFrame) -> bool:
        try:
            expected_numerical_cols = self.__scehma_config["numerical_columns"]
            if not all(col in dataframe.columns for col in expected_numerical_cols):
                logging.error("Not all required numerical columns are present in the DataFrame.")
                return False

            for col in expected_numerical_cols:
                if not pd.api.types.is_numeric_dtype(dataframe[col]):
                    logging.error(f"Column {col} is not numeric.")
                    return False
            logging.info("All required numerical columns are present and numeric.")
            return True
        except Exception as e:
            raise NetworkSecurityException(str(e))

    @staticmethod
    def read_data(filepath)-> pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise NetworkSecurityException(str(e))

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1, d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column: {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found

                }})

            drift_report_file_path = self.data_validation_config.drift_report_file_path

            # Create directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report, )
            return status

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> 'DataValidationArtifact':
        try:
            # Initialize variables


            # Paths for train and test data
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns for train and test DataFrame
            if not self.validate_no_of_cols(dataframe=train_dataframe):
                logging.info("Train dataframe does not contain all required columns.\n")
            if not self.validate_no_of_cols(dataframe=test_dataframe):
                logging.info("Test dataframe does not contain all required columns.\n")


            # Check for data drift
            drift_status = self.detect_dataset_drift(base_df=train_dataframe, current_df=test_dataframe)

            # Create directory for validated files
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path, index=False, header=True
            )

            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path, index=False, header=True
            )

            # Prepare DataValidationArtifact
            data_validation_artifact = DataValidationArtifact(
                validation_status=drift_status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact

        except Exception as e:
            logging.error(f"Error during data validation: {str(e)}")
            raise NetworkSecurityException(e, sys)
