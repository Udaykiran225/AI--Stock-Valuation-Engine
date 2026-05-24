# backend/app/models.py
from datetime import datetime, timezone

class StockCacheModel:
    """Defines the rigid schema structural mapping for the SQLite data layer."""
    def __init__(self, data_dict: dict):
        self.ticker = data_dict.get("ticker", "").upper()
        self.company_name = data_dict.get("company_name", "N/A")
        self.current_price = float(data_dict.get("current_price", 0.0))
        self.trailing_pe = str(data_dict.get("trailing_pe", "N/A"))
        self.debt_to_equity = str(data_dict.get("debt_to_equity", "N/A"))
        self.free_cash_flow = str(data_dict.get("free_cash_flow", "N/A"))
        self.summary = data_dict.get("summary", "No profile summary registry available.")
        self.ai_health_score = float(data_dict.get("ai_health_score", 0.0))
        self.ai_sentiment = data_dict.get("ai_sentiment", "Neutral")
        self.ai_sentiment_score = float(data_dict.get("ai_sentiment_score", 0.0))
        self.parsed_headline = data_dict.get("parsed_headline", "N/A")
        # Modern Python timezone-aware UTC convention:
        self.cached_at = data_dict.get("cached_at", datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return self.__dict__