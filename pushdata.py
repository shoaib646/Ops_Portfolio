"""
Project: MLOps Portfolio Project
Author: Shoaib Shaikh

Purpose: This module is responsible to data from local system to mongodb atlas

Date created:
December 24, 2024
"""
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from pymongo.mongo_client import MongoClient
from pymongo.errors import BulkWriteError
from dotenv import load_dotenv
from typing import List
import pandas as pd
import numpy as np
import certifi
import json
import sys
import os
from networksecurity.constant import  variables


load_dotenv()

class NetworkDataExtractor:

    def __init__(self):
        try:



            mongo_url = os.environ.get("MONGO_URL")
            csv_path = os.path.join("Ops_Portfolio/Dataset", variables.FILENAME)
            db_name = os.environ.get("DB_NAME")
            collection_name = os.environ.get("COLLECTION_NAME")

            if not all([mongo_url, csv_path, db_name, collection_name]):
                raise ValueError("Missing required environment variables.")

            self.client = MongoClient(mongo_url, tlsCAFile=certifi.where())
            self.csv_filepath = csv_path
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]

            logging.info(f"Connected to MongoDB: {mongo_url}, DB: {db_name}, Collection: {collection_name}")

        except Exception as e:
            raise NetworkSecurityException(f"Initialization error: {e}", sys)

    def csv2json(self) -> List[dict]:
        """
        Convert a CSV file to a JSON-compatible list of dictionaries.
        :return: List of dictionaries representing the CSV data.
        """
        try:

            if not os.path.exists(self.csv_filepath):
                raise FileNotFoundError(f"CSV file not found: {self.csv_filepath}")

            data = pd.read_csv(self.csv_filepath)
            if data.empty:
                raise ValueError("CSV file is empty.")

            logging.info(f"Successfully loaded CSV file: {self.csv_filepath}")
            return list(json.loads(data.T.to_json()).values())

        except Exception as e:
            raise NetworkSecurityException(f"CSV to JSON conversion error: {e}", sys)

    def pushdata2mongo(self, records: List[dict]) -> int:
        """
        Insert multiple records into a MongoDB collection.
        :param records: A list of dictionaries representing MongoDB documents.
        :return: The number of successfully inserted records.
        """
        if not records:
            logging.warning("No records provided for insertion.")
            return 0

        try:

            result = self.collection.insert_many(records, ordered=False)
            inserted_count = len(result.inserted_ids)
            logging.info(f"Successfully inserted {inserted_count} records into collection '{self.collection.name}'.")
            return inserted_count
        except BulkWriteError as bwe:
            logging.error(f"Bulk write error occurred: {bwe.details}")
            raise NetworkSecurityException(f"Bulk write error: {bwe.details}", sys)

        except Exception as e:
            logging.error("An error occurred while inserting records into MongoDB.")
            raise NetworkSecurityException(e, sys.exc_info()[2])


if __name__ == "__main__":
    try:
        data_object = NetworkDataExtractor()
        records = data_object.csv2json()
        no_of_records = data_object.pushdata2mongo(records)
    except Exception as e:
        print(e)
        logging.error(f"An error occurred: {e}")

