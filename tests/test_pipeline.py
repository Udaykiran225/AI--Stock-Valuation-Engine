# backend/app/tests/test_pipeline.py
import unittest
from backend.app.services.analyzer import FinancialAnalyzer
from backend.app.models import StockCacheModel

class TestAlphaEnginePipeline(unittest.TestCase):
    
    def test_financial_analyzer_low_risk(self):
        """Verifies that secure multiples return a baseline stable risk tier."""
        result = FinancialAnalyzer.evaluate_investment_risk(pe_ratio=15.0, debt_to_equity=50.0)
        self.assertEqual(result["risk_tier"], "Stable / Baseline")
        self.assertEqual(result["flags"], ["No baseline fundamental risk flags triggered."])

    def test_financial_analyzer_elevated_risk(self):
        """Verifies that crossing thresholds flags severe multiple alerts."""
        result = FinancialAnalyzer.evaluate_investment_risk(pe_ratio=45.0, debt_to_equity=200.0)
        self.assertEqual(result["risk_tier"], "Elevated Structural Risk")
        self.assertTrue(any("Premium Valuation" in flag for flag in result["flags"]))
        self.assertTrue(any("Aggressive Leverage" in flag for flag in result["flags"]))

    def test_model_serialization(self):
        """Ensures the StockCacheModel correctly maps property dictionaries safely."""
        sample_payload = {
            "ticker": "TSLA",
            "company_name": "Tesla Inc.",
            "current_price": 180.00,
            "trailing_pe": "30.5",
            "ai_health_score": 0.85
        }
        model_instance = StockCacheModel(sample_payload)
        output_dict = model_instance.to_dict()
        
        self.assertEqual(output_dict["ticker"], "TSLA")
        self.assertEqual(output_dict["ai_health_score"], 0.85)
        self.assertEqual(output_dict["summary"], "No profile summary registry available.")

if __name__ == "__main__":
    unittest.main()