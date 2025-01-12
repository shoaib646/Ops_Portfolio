import os, sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.constant.variables import  *

# fast api

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from uvicorn import run as uvicorn_run
from starlette.responses import RedirectResponse

##
import pandas as pd
from networksecurity.pipeline.TrainingPipeline import TrainingPipeline


app = FastAPI()
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"],
                   allow_credentials=True)


@app.get("/", tags=["authentication"])
async def root():
    return RedirectResponse(url="/docs")

@app.get("/train", tags=["train"])
async def train():
    try:
        train_pipeline = TrainingPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
    except NetworkSecurityException as e:
        raise NetworkSecurityException(str(e))

# @app.get("/predict", tags=["predict"])
# async def predict(request: Request, file: UploadFile = File(...)):
#     try:
#         df=pd.read_csv(file.file)
#     except NetworkSecurityException as e:
#         raise NetworkSecurityException(str(e))



if __name__ == "__main__":
    uvicorn_run(app, host=HOSTNAME, port=PORT)

