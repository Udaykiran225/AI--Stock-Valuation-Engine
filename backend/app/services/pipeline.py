# backend/app/services/pipeline.py
import yfinance as yf
from backend.app.database import get_db_connection
from backend.app.models import StockCacheModel
from ml_core.inference_nlp import analyze_market_sentiment
from ml_core.train_classifier import calculate_financial_health

class DataOrchestrationPipeline:
    """Manages the full ETL ingest cycle: Fetching web metrics, processing ML inferences, and database writes."""

    @staticmethod
    def execute_pipeline(ticker: str) -> dict:
        clean_ticker = ticker.strip().upper()
        
        # 1. Scraping Core Financials from Global Networks
        stock = yf.Ticker(clean_ticker)
        info = stock.info
        
        if not info or "regularMarketPrice" not in info and "currentPrice" not in info:
            raise ValueError(f"Ticker symbol {clean_ticker} returned zero operational records from financial data networks.")

        pe = info.get("trailingPE")
        de = info.get("debtToEquity")
        
        # Format variables cleanly for standard display strings
        display_pe = round(float(pe), 2) if pe else "N/A"
        display_de = round(float(de), 2) if de else "N/A"
        fcf = info.get("freeCashflow", "N/A")
        if isinstance(fcf, (int, float)):
            fcf = f"${fcf:,.0f}"

        # 2. Run Python ML Models Inferences
        health_score = calculate_financial_health(pe, de)
        nlp_results = analyze_market_sentiment(clean_ticker)

        # 3. Process records through our Model schema mapping layer
        processed_data = StockCacheModel({
            "ticker": clean_ticker,
            "company_name": info.get("longName", "N/A"),
            "current_price": info.get("currentPrice") or info.get("regularMarketPrice", 0.0),
            "trailing_pe": str(display_pe),
            "debt_to_equity": str(display_de),
            "free_cash_flow": str(fcf),
            "summary": info.get("longBusinessSummary", "No corporate profiling data compiled."),
            "ai_health_score": health_score,
            "ai_sentiment": nlp_results["sentiment_verdict"],
            "ai_sentiment_score": nlp_results["sentiment_score"],
            "parsed_headline": nlp_results["top_headline_parsed"]
        })

        # 4. Persistence Phase: Save record straight down to local SQLite binary
        conn = get_db_connection()
        cursor = conn.cursor()
        
        payload = processed_data.to_dict()
        cursor.execute("""
            INSERT OR REPLACE INTO stock_cache (
                ticker, company_name, current_price, trailing_pe, debt_to_equity, 
                free_cash_flow, summary, ai_health_score, ai_sentiment, 
                ai_sentiment_score, parsed_headline, cached_at
            ) VALUES (
                :ticker, :company_name, :current_price, :trailing_pe, :debt_to_equity, 
                :free_cash_flow, :summary, :ai_health_score, :ai_sentiment, 
                :ai_sentiment_score, :parsed_headline, :cached_at
            )
        """, payload)
        
        conn.commit()
        conn.close()
        
        return payload