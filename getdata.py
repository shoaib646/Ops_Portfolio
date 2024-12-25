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

client = MongoClient(os.environ.get("MONGO_URL"))
ca = certifi.where()

class NetworkDataExtractor():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def csv2json(self,csv_filepath) -> List[dict]:
        """

        :param csv_file: 
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def pushdata2mongo(self,db) -> int:
        """

        :param df: 
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

if __name__ == "__main__":
    object = NetworkDataExtractor()
    logging.log(logging.INFO, "Pinged MongoDB")

