"""
Project: MLOps Portfolio Project
Author: Shoaib Shaikh

Purpose: This module is responsible to run end to end training pipeline

Date created:
December 25, 2024
"""

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.pipeline.TrainingPipeline import  TrainingPipeline
import os
import sys



def main():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e,  sys.exc_info()[2])

if __name__ == '__main__':
    main()