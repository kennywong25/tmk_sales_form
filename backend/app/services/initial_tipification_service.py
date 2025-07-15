# app/services/initial_tipification_service.py

from datetime import datetime
from app.bigquery.writer import insert_raw
from loguru import logger

def record_initial_event(payload: dict):
    """
    Registra el evento que abre el formulario (sin tipificar aún).
    Inserta en sales_events_raw con timestamp de apertura.
    """
    row = {
        "event_timestamp": datetime.utcnow().isoformat(),
        "data": payload,
    }
    insert_raw(row)
    logger.info("Evento inicial registrado en sales_events_raw.")
