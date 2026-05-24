import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "stock_data.db")

def get_db_connection():
    """Establishes a standard connection to the local SQLite binary file."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enables accessing columns by name like a dictionary
    return conn

def init_db():
    """Creates the data warehouse cache table structure if it doesn't exist."""
    # Ensure the backend/data directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_cache (
            ticker TEXT PRIMARY KEY,
            company_name TEXT,
            current_price REAL,
            trailing_pe TEXT,
            debt_to_equity TEXT,
            free_cash_flow TEXT,
            summary TEXT,
            ai_health_score REAL,
            ai_sentiment TEXT,
            ai_sentiment_score REAL,
            parsed_headline TEXT,
            cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("🗄️ SQLite Stock Cache Database initialized successfully!")

if __name__ == "__main__":
    init_db()
    