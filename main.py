import os, sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.utils.ML.model.estimator import ModelResolver
from networksecurity.constant.variables import SAVED_MODEL_DIR
from networksecurity.utils.Main.utils import load_object
from networksecurity.constant.variables import  *

# fast api

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from uvicorn import run as uvicorn_run
from starlette.responses import RedirectResponse

##
import pandas as pd
from networksecurity.pipeline.TrainingPipeline import TrainingPipeline

templates = Jinja2Templates(directory="./templates")


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

# @app.post("/predict")
# async def predict_route(request: Request, file: UploadFile = File(...)):
#     try:
#         df = pd.read_csv(file.file)
#         # print(df)
#         model = ModelResolver(model_dir=SAVED_MODEL_DIR)
#         latest_model_path = model.get_best_model_path()
#         latest_model = load_object(file_path=latest_model_path)
#
#         y_pred = latest_model.predict(df)
#         df['predicted_column'] = y_pred
#         df['predicted_column'].replace(-1, 0)
#         # return df.to_json()
#         table_html = df.to_html(classes='table table-striped')
#         # print(table_html)
#         return templates.TemplateResponse("table.html", {"request": request, "table": table_html})
#
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)



if __name__ == "__main__":
    uvicorn_run(app, host=HOSTNAME, port=PORT)

