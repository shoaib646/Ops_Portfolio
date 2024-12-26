"""
Project: MLOps Portfolio Project
Author: Shoaib Shaikh

Purpose: This module is responsible inject data from mongodb to model

Date created:
December 25, 2024
"""
import numpy as np
import pandas as pd

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.config import DataIngestionConfig
from networksecurity.entity.artifact import DataIngestionArtifact

import pandas
import numpy
import os
import sys
import pymongo
from typing import List, Tuple
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split


load_dotenv()


class DataIngestion():

    def __init__(self, data_ingestion_config):
        self.split_ratio = None
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def export_collection_as_df(self) -> pandas.DataFrame:
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            self.mongo_client = pymongo.MongoClient(os.environ.get('MONGO_URL'))
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop(columns=["_id"], axis=1, inplace=True)
            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def export_data2featurestore(self, dataframe:pd.DataFrame)-> pandas.DataFrame:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def split_data(self, dataframe:pandas.DataFrame):
        try:
            self.split_ratio = self.data_ingestion_config.train_test_split_ratio

            train_set, test_set = train_test_split(dataframe, test_size=self.split_ratio,shuffle=True,
                                                   random_state=42)
            logging.info("Performed train test split on the dataframe")
            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info(f"Exported train and test file path.")

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def initiate_data_ingestion(self):
        try:

            dataframe = self.export_collection_as_df()
            dataframe = self.export_data2featurestore(dataframe)
            self.split_data(dataframe)

            output = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path)

            return output

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

