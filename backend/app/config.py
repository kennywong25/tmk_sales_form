# app/config.py
from pydantic import BaseSettings
from google.cloud import bigquery

class Settings(BaseSettings):
    gcp_project: str
    bq_dataset: str
    bq_table_raw: str
    bq_table_completed: str
    bq_table_dev: str

    env: str = "prod"

settings = Settings()
bq_client = bigquery.Client(project=settings.gcp_project)
