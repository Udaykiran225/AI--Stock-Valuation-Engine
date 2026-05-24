# backend/app/services/analyzer.py

class FinancialAnalyzer:
    """Executes programmatic fundamental analysis calculations on core equity metrics."""
    
    @staticmethod
    def evaluate_investment_risk(pe_ratio, debt_to_equity) -> dict:
        """
        Calculates institutional risk grading tiers based on fundamental parameters.
        """
        reasons = []
        
        # Parse inputs safely
        try:
            clean_pe = float(pe_ratio) if pe_ratio not in ["N/A", None] else None
            clean_de = float(debt_to_equity) if debt_to_equity not in ["N/A", None] else None
        except ValueError:
            return {"risk_tier": "High Variance", "flags": ["Invalid balance sheet metric formatting."]}

        # Check for premium valuation risk flags
        if clean_pe and clean_pe > 35:
            reasons.append(f"Premium Valuation Multiplier Alert: P/E of {clean_pe} indicates high speculative premium.")
        
        # Check for structural debt leverage flags
        if clean_de and clean_de > 150:
            reasons.append(f"Aggressive Leverage Alert: Debt-to-Equity scale of {clean_de}% points to heavy balance sheet liabilities.")

        if len(reasons) == 0:
            tier = "Stable / Baseline"
        elif len(reasons) == 1:
            tier = "Moderate Risk Divergence"
        else:
            tier = "Elevated Structural Risk"

        return {
            "risk_tier": tier,
            "flags": reasons if reasons else ["No baseline fundamental risk flags triggered."]
        }