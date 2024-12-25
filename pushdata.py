from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from  dotenv import load_dotenv
from typing import List
import sys
import os
import json
import certifi
import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient

load_dotenv()

ca = certifi.where()

class NetworkDataExtractor():

    def __init__(self):

        try:

            self.client = MongoClient(os.environ.get("MONGO_URL"))
            self.csv_filepath = os.environ.get("CSV_PATH")
            self.db = self.client[os.environ.get("DB_NAME")]
            self.collection = self.db[os.environ.get("COLLECTION_NAME")]

        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def csv2json(self) -> List[dict]:
        """

        :param csv_file: 
        """
        try:
            data = pd.read_csv(self.csv_filepath)
            data.reset_index(drop=True, inplace=True)
            return list(json.loads(data.T.to_json()).values())


        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def pushdata2mongo(self,records) -> int:
        """

        :param df: 
        """
        try:
            self.collection.insert_many(records)
            logging.info("Inserted records into mongo")
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

if __name__ == "__main__":
    Dataobject = NetworkDataExtractor()
    records = Dataobject.csv2json()
    noofrecords = Dataobject.pushdata2mongo(records)
    print("No of Records in MongoDB:",noofrecords)

