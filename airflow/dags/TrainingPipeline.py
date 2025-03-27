from asyncio import tasks
import json
from textwrap import dedent
import pendulum
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from dotenv import load_dotenv

load_dotenv()

with DAG(
        'url_security',
        default_args={'retries': 2},
        # [END default_args]
        description='url security pipeline',
        schedule_interval="@weekly",
        start_date=pendulum.datetime(2025, 4, 27, tz="UTC"),
        catchup=False,
        tags=['example'],
) as dag:
    def training(**kwargs):
        from networksecurity.pipeline.TrainingPipeline import TrainingPipeline
        training_obj = TrainingPipeline()
        training_obj.run_pipeline()


    # def sync_artifact_to_s3_bucket(**kwargs):
    #     bucket_name = os.getenv('S3_BUCKET_NAME')
    #     os.system(f"aws s3 sync /app/Artifacts s3://{bucket_name}/artifact")
    #     os.system(f"aws s3 sync /app/saved_models s3://{bucket_name}/saved_models")

    def sync_artifact_to_s3_bucket(**kwargs):
        bucket_name = os.getenv("S3_BUCKET_NAME")
        if not bucket_name:
            raise Exception("Environment variable 'S3_BUCKET_NAME' is not set.")

        artifact_result = os.system(f"aws s3 sync /app/Artifacts s3://{bucket_name}/artifact")
        if artifact_result != 0:
            raise Exception("Failed to sync artifacts to S3.")

        model_result = os.system(f"aws s3 sync /app/saved_models s3://{bucket_name}/saved_models")
        if model_result != 0:
            raise Exception("Failed to sync models to S3.")


    training_pipeline = PythonOperator(
        task_id="train_pipeline",
        python_callable=training

    )

    sync_data_to_s3 = PythonOperator(
        task_id="sync_data_to_s3",
        python_callable=sync_artifact_to_s3_bucket

    )

    training_pipeline >> sync_data_to_s3