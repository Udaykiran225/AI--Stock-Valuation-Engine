import numpy as np
import pandas as pd
from xgboost import XGBClassifier
import joblib
import os

# Define the file path where we will save our trained model weights
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "xgboost_health_model.pkl")

def build_and_train_model():
    """
    Generates a synthetic financial dataset based on institutional risk baselines
    and trains an XGBoost classifier to predict corporate safety.
    """
    np.random.seed(42)
    num_samples = 1000
    
    # Generate random realistic P/E Ratios (ranging from 5 to 60)
    pe_ratios = np.random.uniform(5, 60, num_samples)
    # Generate random realistic Debt-to-Equity percentages (ranging from 10% to 250%)
    debt_to_equity = np.random.uniform(10, 250, num_samples)
    
    # Define an institutional safety ground-truth rule:
    # A company is classified as "Healthy" (1) if it doesn't combine massive debt with massive valuation multiples.
    # Otherwise, it's classified as "Risky" (0).
    labels = np.where((pe_ratios < 35) & (debt_to_equity < 120), 1, 0)
    
    # Structure into a training DataFrame
    df = pd.DataFrame({
        'pe_ratio': pe_ratios,
        'debt_to_equity': debt_to_equity,
        'label': labels
    })
    
    X = df[['pe_ratio', 'debt_to_equity']]
    y = df['label']
    
    # Initialize and train the XGBoost Classification tree
    model = XGBClassifier(n_estimators=50, max_depth=3, random_state=42, eval_metric='logloss')
    model.fit(X, y)
    
    # Ensure the models directory exists and save the trained weights
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print("🚀 XGBoost Financial Health Model trained and saved successfully!")

def calculate_financial_health(pe_ratio, debt_to_equity) -> float:
    """
    Loads the trained XGBoost model and executes an active inference pass
    to return a mathematical safety probability score between 0.0 and 1.0.
    """
    # If the saved model file doesn't exist yet, train it on the fly
    if not os.path.exists(MODEL_PATH):
        build_and_train_model()
        
    # Load the saved model weights
    model = joblib.load(MODEL_PATH)
    
    # Handle missing incoming data points from the API gracefully
    clean_pe = float(pe_ratio) if pe_ratio not in ["N/A", None] else 20.0
    clean_de = float(debt_to_equity) if debt_to_equity not in ["N/A", None] else 70.0
    
    # Format features for structural model prediction
    features = pd.DataFrame([[clean_pe, clean_de]], columns=['pe_ratio', 'debt_to_equity'])
    
    # Predict the probability distribution probabilities [[probability_of_0, probability_of_1]]
    probabilities = model.predict_proba(features)[0]
    
    # Return the safety probability score (Class 1) rounded cleanly
    return round(float(probabilities[1]), 2)

if __name__ == "__main__":
    # Running the script standalone triggers a fresh model training sequence
    build_and_train_model()