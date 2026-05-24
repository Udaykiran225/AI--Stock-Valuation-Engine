# AlphaEngine // AI-Driven Stock Valuation & Risk Architecture

AlphaEngine is an enterprise-grade, full-stack microservices application that orchestrates an automated ETL (Extract, Transform, Load) data pipeline. It ingests live equity profiles from market data networks and executes a multi-threaded hybrid Machine Learning pipeline (XGBoost Classifier + FinBERT NLP Neural Network Transformer) to evaluate structural balance sheet safety index limits alongside active textual market news sentiment.

## 📁 Project Directory Structure
~~~

The repository is organized following industry-standard design patterns, cleanly separating frontend presentation, backend routing logic, and data engineering layers:
STOCK_AI/
├── backend/
│   └── app/
│       ├── api/
│       │   └── stocks.py           # Sub-routed stock intelligence endpoint logic
│       ├── services/
│       │   ├── analyzer.py         # Programmatic fundamental risk grading matrix
│       │   └── pipeline.py         # ETL pipeline controller (Scrape -> ML -> Cache)
│       ├── database.py             # SQLite data warehouse connection & table initialization
│       ├── main.py                 # FastAPI system core application gateway
│       ├── models.py               # Rigid data property cache mapping schema
│       └── schemas.py              # Pydantic JSON contract data enforcement layers
├── frontend/
│   ├── components/
│   │   └── utils.py                # Contextual UI warning alert visual components
│   └── app.py                      # Streamlit graphical analytics dashboard interface
├── ml_core/
│   ├── models/
│   │   ├── finbert_config/         # FinBERT local caching parameters
│   │   └── xgboost_health_model.pkl # Offline-trained operational classifier binary
│   ├── inference_nlp.py            # Real-time text scraping and transformer scoring
│   └── train_classifier.py         # XGBoost model fitting and fundamental scoring math
├── tests/
│   └── test_pipeline.py            # Automated Unit testing validation suite
├── .gitignore                      # Configuration file tracking repository exclusion rules
├── README.md                       # Comprehensive platform deployment documentation
└── requirements.txt                # Fixed framework dependencies manifest file
~~~

## 🏗️ System Architecture & Data Flow

The application is engineered using a decoupled, modular microservices layout to ensure clean separation of concerns:

- **Frontend Interface Panel (`frontend/`):** A responsive Streamlit dashboard configured with clean custom CSS layout modules, grid-stat containers, and real-time interactive multi-threaded data visualizations using Plotly.
- **API Gatekeeper Gateway (`backend/app/main.py`):** A high-performance FastAPI core routing requests dynamically through specialized sub-routers (`api/stocks.py`).
- **Data Orchestration Pipeline (`services/pipeline.py`):** A structured data controller handling the full lifecycle of data validation via Pydantic (`schemas.py`), internal struct mapping (`models.py`), and analytics processing (`services/analyzer.py`).
- **Persistence Storage Cache (`backend/data/`):** A localized SQLite database cache designed to eliminate redundant network latency and protect against web rate-limiting by instantly handling warehouse cache hits.
- **Machine Learning Layer (`ml_core/`):** - **Quantitative:** An offline-compiled binary XGBoost tree model checking equity multipliers.
  - **Qualitative:** A deep-learning FinBERT text transformer mapping real-time RSS semantic trends.

---

## 🚀 Local Installation & Deployment Guide

Follow these sequential steps to initialize, test, and deploy the entire platform ecosystem locally on your machine:

### 1. Environment Synchronization
Clone this repository to your local system workspace, initialize a Python virtual environment, and install the compiled requirements tracking list:
~~~
# Initialize and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install synchronized project dependencies
pip install -r requirements.txt
~~~
2. Database & Module Initialization
Run the initialization scripts to generate the tracking data arrays and establish your local SQL warehouse caching tables:
~~~
# Compile and train the local binary classification model
python3 ml_core/train_classifier.py

# Physically initialize the local SQLite database cache binary
python3 backend/app/database.py
~~~

3. Running Automated Quality Control Tests
Verify that all mathematical risk calculators, dictionary serialization models, and structural filters match operational criteria using the pytest suite wrapper:
~~~
python3 -m pytest tests/test_pipeline.py
~~~

5. Launching the Microservice Clusters
To boot up the complete active environment, open two separate terminal panels inside your code workspace to activate both listeners simultaneously:
Terminal Tab A: FastAPI Backend Routing Engine
~~~
uvicorn backend.app.main:app --reload
~~~

Once running, you can explore the dynamically compiled interactive API documentation directly via the Swagger UI panel at: http://127.0.0.1:8000/docs
Terminal Tab B: Streamlit Graphical Interface Panel
~~~
streamlit run frontend/app.py
~~~

The engine will automatically open your local browser to http://localhost:8501. Enter any ticker symbol (e.g., AAPL, NVDA, TSLA) to trigger the live inference pipeline.
🔬 Core Interface Schema Specifications
The backend validation engine enforces explicit JSON API data contracts via Pydantic to ensure reliable communication boundaries:
~~~
{
  "ticker": "string",
  "company_name": "string",
  "current_price": 0.0,
  "trailing_pe": "string",
  "debt_to_equity": "string",
  "free_cash_flow": "string",
  "summary": "string",
  "ai_health_score": 0.0,
  "ai_sentiment": "string",
  "ai_sentiment_score": 0.0,
  "parsed_headline": "string",
  "cached_at": "string (ISO Timestamp)"
}
~~~

🛠️ Technology Stack Inventory
•	UI Framework: Streamlit, Plotly JavaScript Graphing Engine
•	Asynchronous Routing Gateway: FastAPI, Uvicorn Server Core, Pydantic v2
•	Data Engineering Warehouse: SQLite3, Structured Query Language Modules, YFinance
•	Machine Learning Frameworks: Core PyTorch Model Weights, XGBoost Classifier, Scikit-Learn Ecosystem, HuggingFace Transformers

---
~~~

### Push the Updated Repository to GitHub

Save the file (`Cmd + S`) and run these three quick commands in your terminal to sync the file structure straight up to your live profile:

```bash
git add README.md
git commit -m "docs: add structural project directory map to README"
git push origin main
~~~
