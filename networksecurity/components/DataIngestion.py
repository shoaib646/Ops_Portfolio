"""
Project: MLOps Portfolio Project
Author: Shoaib Shaikh

Purpose: This module is responsible inject data from mongodb to model

Date created:
December 25, 2024
"""

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

from pymongo.mongo_client import MongoClient
import certifi

load_dotenv()


class DataIngestion():

    def __init__(self):

        try:
            mongo_url = os.environ.get("MONGO_URL")


        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def export_collection_as_df(self):
        try:
            documents = self.collection.find()

        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def export_data2featurestore(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def split_data(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys.exc_info()[2])