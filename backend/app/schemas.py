# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional

class StockAnalysisResponse(BaseModel):
    """Rigid validation layer defining API JSON output structures."""
    ticker: str
    company_name: str
    current_price: float
    trailing_pe: str
    debt_to_equity: str
    free_cash_flow: str
    summary: str
    ai_health_score: float
    ai_sentiment: str
    ai_sentiment_score: float
    parsed_headline: str
    cached_at: Optional[str] = None