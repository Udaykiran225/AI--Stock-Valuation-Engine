# backend/app/api/stocks.py
from fastapi import APIRouter, HTTPException
from backend.app.database import get_db_connection
from backend.app.services.pipeline import DataOrchestrationPipeline
from backend.app.schemas import StockAnalysisResponse

router = APIRouter(prefix="/api/stock", tags=["Stock Intelligence Layer"])

@router.get("/{ticker}", response_model=StockAnalysisResponse)
def query_stock_analytics(ticker: str):
    """Handles stock data queries by prioritizing database lookups before falling back to live execution pipelines."""
    clean_ticker = ticker.strip().upper()
    if not clean_ticker.isalnum() or len(clean_ticker) > 5:
        raise HTTPException(status_code=400, detail="Invalid global stock ticker structural formatting constraints.")

    # A. Check Local Warehouse Database Cache
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stock_cache WHERE ticker = ?", (clean_ticker,))
    row = cursor.fetchone()
    
    if row:
        print(f"🎯 Warehouse Cache Hit! Serving structural record for {clean_ticker} instantly.")
        cached_data = dict(row)
        conn.close()
        return cached_data

    # B. Cache Miss Flow: Trigger our new pipeline module to do the heavy pulling/ML processing
    conn.close()
    print(f"⚡ Warehouse Cache Miss! Activating live data pipeline orchestrator for {clean_ticker}...")
    try:
        data_payload = DataOrchestrationPipeline.execute_pipeline(clean_ticker)
        return data_payload
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Ecosystem Pipeline Processing Fault: {str(e)}")