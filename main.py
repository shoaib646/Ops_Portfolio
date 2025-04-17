

import os
import sys
import pandas as pd
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from uvicorn import run as uvicorn_run

# Project imports
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.utils.ML.model.estimator import ModelResolver
from networksecurity.constant.variables import SAVED_MODEL_DIR
from networksecurity.utils.Main.utils import load_object
from networksecurity.pipeline.TrainingPipeline import 
from networksecurity.constant.variables import  *

app = FastAPI(title="PhishShield AI", description="MLOps for Cybersecurity URL Classification")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Security theme colors
THEME_COLORS = {
    "primary": "#008000",
    "secondary": "#5DA9E9",
    "danger": "#E63946",
    "success": "#4CAF50"
}

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "theme": THEME_COLORS
    })

@app.get("/analyze", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "theme": THEME_COLORS
    })

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, file: UploadFile = File(...)):
    try:

         # Validate file was uploaded
        if not file.filename:
            raise NetworkSecurityException("No file uploaded", error_details="Please select a file before submitting")
            
        # Validate file type
        if not file.filename.lower().endswith('.csv'):
            raise NetworkSecurityException("Invalid file type", error_details="Only CSV files are supported")

        # Validate file type
        if not file.filename.endswith(".csv"):
            raise NetworkSecurityException("Only CSV files are allowed")
        
        # Show processing status
        processing_template = templates.TemplateResponse("processing.html", {
            "request": request,
            "theme": THEME_COLORS,
            "filename": file.filename
        })
        
        # Process file
        df = pd.read_csv(file.file)
        
        # Model prediction
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=model_path)
        
        # Original prediction logic
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'] = df['predicted_column'].replace(-1, 0)
        
        # Add status labels with security icons
        df['Status'] = df['predicted_column'].apply(
            lambda x: "🛡️ Legitimate" if x == 0 else "🔥 Phishing Detected"
        )
        
        # Generate interactive table
        table_html = df.iloc[:-1].to_html(
            classes="table table-striped table-bordered table-hover",
            index=False,
            columns=list(df.columns[:-1]) + ['Status'],
            escape=False
        )
        
        # Generate security statistics
        stats = {
            "total": len(df),
            "legitimate": len(df[df['predicted_column'] == 0]),
            "phishing": len(df[df['predicted_column'] == 1]),
            "phishing_percent": (len(df[df['predicted_column'] == 1]) / len(df)) * 100
        }
        
        return templates.TemplateResponse("results.html", {
            "request": request,
            "theme": THEME_COLORS,
            "filename": file.filename,
            "table": table_html,
            "stats": stats
        })
        
    except Exception as e:
        logging.error(f"Analysis error: {str(e)}")
        return templates.TemplateResponse("error.html", {
            "request": request,
            "theme": THEME_COLORS,
            "error_message": f"Security Analysis Failed: {str(e)}"
        })

@app.get("/docs", include_in_schema=False)
async def swagger_docs():
    return RedirectResponse(url="/docs")

# Training endpoint (protected in production)
@app.post("/train")
async def train():
    try:
        train_pipeline = TrainingPipeline()
        if train_pipeline.is_pipeline_running:
            return {"status": "error", "message": "Training already in progress"}
        train_pipeline.run_pipeline()
        return {"status": "success", "message": "Training pipeline started"}
    except NetworkSecurityException as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOSTNAME, port=PORT, reload=True)