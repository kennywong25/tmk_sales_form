from fastapi import FastAPI
from app.routes.ventas import router as ventas_router

app = FastAPI(title="API Wolkvox → BigQuery")
app.include_router(ventas_router)
