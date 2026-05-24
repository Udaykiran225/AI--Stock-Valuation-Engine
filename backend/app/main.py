# backend/app/main.py
import os
# Structural Multi-Threading Safe Enforcements for Apple Silicon Hardware Layers
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import init_db
from backend.app.api.stocks import router as stock_intelligence_router

# Initialize the App instance
app = FastAPI(
    title="AlphaEngine // Quantitative Intelligence API Core",
    description="Enterprise Multi-Model Analytics Microservice for Asset Valuation",
    version="2.0.0"
)

# Connect cross-origin browser communication networks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database schemas when application boots
@app.on_event("startup")
def application_startup_sequence():
    init_db()

# Mount our modular stock intelligence router file directly into the application server core
app.include_router(stock_intelligence_router)

@app.get("/")
def systems_health_check():
    return {"status": "operational", "architecture_tier": "modular_microservices"}