from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from  dotenv import load_dotenv
import sys
import os
import json
import certifi
import pandas as pd
import numpy as np
import pymongo



load_dotenv()

MongoURL = os.environ.get("MONGO_URL")
ca = certifi.where()


class NetworkDataExtractor():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def csv2json(self,csv_file) -> object:
        """

        :param csv_file: 
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

    def pushdata2mongo(self,df) -> object:
        """

        :param df: 
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys.exc_info()[2])

