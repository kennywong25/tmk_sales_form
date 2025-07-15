# app/services/tipification_data_service.py

from datetime import datetime
from app.bigquery.writer import insert_completed
from loguru import logger

def record_tipification(original_payload: dict, agent_details: dict):
    """
    Guarda en sales_events_completed:
      - timestamp de apertura (del original)
      - timestamp de completion (ahora)
      - todos los campos originales
      - detalles tipificados por el agente
    """
    row = {
        "event_timestamp": original_payload.get("event_timestamp"),
        "completion_timestamp": datetime.utcnow().isoformat(),
        **original_payload.get("data", {}),
        **agent_details,
    }
    insert_completed(row)
    logger.info("Datos de tipificación guardados en sales_events_completed.")
