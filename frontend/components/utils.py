# frontend/components/utils.py
import streamlit as st

def render_system_alert(score: float):
    """Renders contextual warning callouts based on pipeline machine learning models parameters."""
    if score >= 0.75:
        st.success("🟢 LOW FUNDAMENTAL RISK: Structural indicators track within safe institutional ranges.")
    elif score >= 0.50:
        st.warning("指标 VARIANCES DETECTED: XGBoost algorithms register minor performance divergence.")
    else:
        st.error("🔴 ELEVATED RISK NOTICE: Company fundamentals fall completely out of safe baseline bounds.")