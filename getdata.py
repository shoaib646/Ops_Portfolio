import sys, os, json
from  dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


load_dotenv()


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
        
    