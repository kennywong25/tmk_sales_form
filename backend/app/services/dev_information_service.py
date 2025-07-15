# app/services/dev_information_service.py
from datetime import datetime
from app.bigquery.writer import insert_dev
from app.config import settings
from loguru import logger

def dev_insert(payload: dict):
    """
    Inserta SOLO si settings.env == "dev".
    """
    if settings.env != "dev":
        logger.warning("dev_insert omitido: no estamos en entorno DEV.")
        return

    row = {
        "data": payload,
    }
    insert_dev(row)
    logger.info("Payload guardado en DEV_EVENTS.")
