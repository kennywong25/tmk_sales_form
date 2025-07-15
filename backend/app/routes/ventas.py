# app/routes/ventas.py

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.services.dev_information_service import dev_insert
from app.services.initial_tipification_service import record_initial_event
from app.services.tipification_data_service import record_tipification

router = APIRouter(prefix="", tags=["ventas"])


@router.post("/dev", status_code=201)
async def dev_endpoint(payload: dict):
    dev_insert(payload)
    return {"status": "ok (dev)"}

@router.post("/ventas/entrada", status_code=201)
async def entrada_venta(payload: dict):
    record_initial_event(payload)
    return {"status": "ok (initial)"}

@router.post("/ventas/confirmacion", status_code=201)
async def confirmacion_venta(body: Dict[str, Any]):
    original = body["original_event"]
    detalles = body["agent_details"]
    record_tipification(original, detalles)
    return {"status": "ok (completed)"}
