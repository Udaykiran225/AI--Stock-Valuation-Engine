import streamlit as st
import requests
import plotly.graph_objects as go
import yfinance as yf
from components.utils import render_system_alert

# Set ultra-wide modern layout and premium page title
st.set_page_config(page_title="AlphaEngine // AI Stock Valuation", layout="wide", initial_sidebar_state="collapsed")

# Inject Custom CSS to give it a dark, sleek, institutional terminal feel
st.markdown("""
    <style>
        .reportview-container { background: #0e1117; }
        .metric-card {
            background-color: #161b22;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #30363d;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        .ai-zone {
            background: linear-gradient(135deg, #1f192f 0%, #161b22 100%);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #8b5cf6;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ AlphaEngine // AI-Driven Valuation & Risk Architecture")
st.markdown("💾 *Enterprise Hybrid Deep Learning Portfolio Pipeline*")
st.markdown("---")

# Centered Search Bar Layout
col_space1, col_search, col_space2 = st.columns([1, 2, 1])
with col_search:
    ticker = st.text_input("ENTER TICKER SYMBOL", max_chars=5, placeholder="e.g. AAPL, NVDA, TSLA").strip().upper()
    run_analysis = st.button("RUN HYBRID QUANT & NLP ANALYSIS", type="primary", use_container_width=True)

if run_analysis and ticker:
    with st.spinner(f"Executing pipeline synchronization for {ticker}..."):
        try:
            # 1. Fetch data from our modular FastAPI sub-routed backend network
            response = requests.get(f"http://127.0.0.1:8000/api/stock/{ticker}")
            
            if response.status_code == 200:
                data = response.json()
                
                # --- SECTION A: COMPANY HERO BANNER ---
                st.markdown(f"## 🏢 {data['company_name']} <span style='color:#8b5cf6;'>[{data['ticker']}]</span>", unsafe_allow_html=True)
                
                # Big Stat Row utilizing clean grid blocks
                m_col1, m_col2, m_col3 = st.columns(3)
                with m_col1:
                    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                    st.metric(label="CURRENT MARKET PRICE", value=f"${data['current_price']:.2f}")
                    st.markdown("</div>", unsafe_allow_html=True)
                with m_col2:
                    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                    st.metric(label="TRAILING P/E RATIO", value=str(data['trailing_pe']))
                    st.markdown("</div>", unsafe_allow_html=True)
                with m_col3:
                    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                    st.metric(label="FREE CASH FLOW", value=str(data['free_cash_flow']))
                    st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                # --- SECTION B: INTERACTIVE CHART ENGINE ---
                st.subheader("📈 Real-Time 6-Month Market Context Matrix")
                try:
                    hist_stock = yf.Ticker(ticker)
                    df_hist = hist_stock.history(period="6mo")
                    
                    if not df_hist.empty:
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(x=df_hist.index, y=df_hist['Close'], name='Closing Price', line=dict(color='#8b5cf6', width=2.5)))
                        fig.update_layout(
                            template="plotly_dark",
                            margin=dict(l=20, r=20, t=20, b=20),
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            xaxis=dict(showgrid=True, gridcolor='#30363d'),
                            yaxis=dict(showgrid=True, gridcolor='#30363d')
                        )
                        st.plotly_chart(fig, on_select="ignore")
                except Exception:
                    st.info("Historical visualization component processing delayed.")

                st.markdown("---")
                
                # --- SECTION C: PREMIUM AI VERDICT SUITE ---
                st.markdown("<div class='ai-zone'>", unsafe_allow_html=True)
                st.subheader("🤖 Hybrid Machine Learning Core Outputs")
                
                ai_col1, ai_col2 = st.columns(2)
                
                with ai_col1:
                    score = data['ai_health_score']
                    st.markdown(f"#### **Quantitative Safety Index: {score * 100}%**")
                    st.progress(score)
                    render_system_alert(score)
                        
                with ai_col2:
                    sentiment = data['ai_sentiment']
                    st.markdown(f"#### **NLP Semantic Core Stream: {sentiment}**")
                    
                    if sentiment == "Bullish":
                        st.info(f"🚀 **LIVE MARKET NEWS SIGNAL:**\n\n*\"{data['parsed_headline']}\"*")
                    elif sentiment == "Neutral":
                        st.info(f"↔️ **LIVE MARKET NEWS SIGNAL:**\n\n*\"{data['parsed_headline']}\"*")
                    else:
                        st.error(f"📉 **LIVE MARKET NEWS SIGNAL:**\n\n*\"{data['parsed_headline']}\"*")
                        
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")
                
                # --- SECTION D: PROFILE BRIEF ---
                st.subheader("🏢 Corporate Operational Profile")
                st.caption(data['summary'])
                
            elif response.status_code == 404:
                # Premium Client-Side Graceful Error Interceptor
                st.warning(f"🔍 Ticker symbol '{ticker}' could not be resolved. Please verify the symbol and try again.")
            else:
                st.error(f"Ecosystem API returned a structural {response.status_code} fault error.")
        except requests.exceptions.ConnectionError:
            st.error("Network gateway timeout: Ensure your FastAPI sub-routed server is running active on Port 8000!")