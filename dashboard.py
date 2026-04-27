
import streamlit as st
import pandas as pd
import plotly.express as px
from bundle_builder.main import BundleBuilderAI, PRODUCTS
from bundle_builder.ab_test import ABTestSimulator

import subprocess

# Initialize
@st.cache_resource
def get_engine():
    return BundleBuilderAI()

@st.cache_resource
def get_simulator():
    return ABTestSimulator()

def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
    except:
        return "main"

engine = get_engine()
simulator = get_simulator()

st.set_page_config(page_title="Bundle Builder AI Decision Lab", layout="wide")

# --- Sidebar ---
st.sidebar.markdown(f"**Build:** `{get_git_hash()}`")
st.sidebar.divider()

# --- Tabs ---
tab_dashboard, tab_ab_test = st.tabs(["🚀 Decision Dashboard", "🧪 A/B Simulation Lab"])

with tab_dashboard:
    st.title("Bundle Builder AI – Decision Intelligence")
    st.markdown("Optimize for **Relevance**, **Revenue**, and **Conversion** in real-time.")

    # --- Sidebar ---
    st.sidebar.header("🛒 Input Configuration")
    selected_product_names = st.sidebar.multiselect(
        "Select Products in Cart",
        options=[p["name"] for p in PRODUCTS],
        default=[PRODUCTS[0]["name"]]
    )
    budget = st.sidebar.number_input("Budget (SAR)", value=1000, step=100)
    baby_age = st.sidebar.selectbox("Baby Age", ["Newborn", "3 months", "6 months", "12 months", "18 months", "2+ years"])
    debug_mode = st.sidebar.toggle("Enable Debug Mode", value=False)
    input_products = [p for p in PRODUCTS if p["name"] in selected_product_names]

    if st.sidebar.button("Generate Optimized Bundles", type="primary"):
        payload = {"products": input_products, "budget": budget, "baby_age": baby_age}
        with st.spinner("Analyzing decisions..."):
            result = engine.process_request(payload)
        
        if not result["bundles"]:
            st.warning("⚠️ No bundles generated.")
        else:
            summary = result["system_summary"]
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Avg AOV Lift", f"{summary['avg_aov_lift']}%")
            col2.metric("Avg Conversion Prob", f"{int(summary['avg_conversion_probability']*100)}%")
            col3.metric("Avg Confidence", f"{int(summary['avg_confidence']*100)}%")
            col4.metric("Bundles Generated", summary['bundles_generated'])
            
            st.divider()
            st.subheader("📈 Decision Intelligence Chart")
            plot_data = pd.DataFrame([{
                "Bundle": f"B{i+1}", "Conversion": b["conversion_probability"], 
                "AOV Lift": b["aov_lift_percent"], "Decision Score": b["decision_score"]
            } for i, b in enumerate(result["bundles"])])
            fig = px.scatter(plot_data, x="Conversion", y="AOV Lift", size="Decision Score", color="Decision Score", text="Bundle", range_x=[0, 1], range_y=[0, 60])
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("🎯 Top Recommended Decisions")
            for i, bundle in enumerate(result["bundles"]):
                with st.container(border=True):
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"### Bundle {i+1}")
                        st.write(f"**Items:** {', '.join([p['name'] for p in bundle['items']])}")
                    with c2:
                        st.metric("Decision Score", bundle["decision_score"])
                    
                    st.write("---")
                    sc1, sc2, sc3, sc4 = st.columns(4)
                    sc1.progress(bundle["debug"]["relevance"], text=f"Relevance: {round(bundle['debug']['relevance'], 2)}")
                    sc2.progress(bundle["debug"]["utility"], text=f"Utility: {round(bundle['debug']['utility'], 2)}")
                    sc3.progress(bundle["debug"]["price_fit"], text=f"Price Fit: {round(bundle['debug']['price_fit'], 2)}")
                    sc4.progress(bundle["debug"]["diversity"], text=f"Diversity: {round(bundle['debug']['diversity'], 2)}")
                    
                    with st.expander("💡 Logic"):
                        st.info(bundle['reasoning_en'])

            if debug_mode:
                st.divider()
                st.json(result)

with tab_ab_test:
    st.title("🧪 A/B Testing Simulation Lab")
    st.markdown("Prove the business impact of AI decisions against a rule-based baseline.")
    
    num_users = st.slider("Number of Simulated Users", 100, 1000, 500)
    
    if st.button("🚀 Run A/B Simulation", type="primary"):
        with st.spinner(f"Simulating {num_users} shopping journeys..."):
            sim_res = simulator.run_simulation(num_users)
            
        st.success("Simulation Complete!")
        
        # Uplift Row
        u1, u2, u3 = st.columns(3)
        u1.metric("Revenue Uplift", f"{sim_res['uplift']['revenue_increase']}%", delta=sim_res['uplift']['revenue_increase'])
        u2.metric("AOV Uplift", f"{sim_res['uplift']['aov_increase']}%", delta=sim_res['uplift']['aov_increase'])
        u3.metric("Conversion Uplift", f"{sim_res['uplift']['conversion_increase']}%", delta=sim_res['uplift']['conversion_increase'])
        
        st.divider()
        
        # Comparison Table
        st.subheader("📊 Comparative Metrics")
        df_comp = pd.DataFrame([
            {"Metric": "Avg AOV (SAR)", "Baseline": sim_res["baseline"]["avg_aov"], "AI System": sim_res["ai_system"]["avg_aov"]},
            {"Metric": "Conversion Rate", "Baseline": sim_res["baseline"]["conversion_rate"], "AI System": sim_res["ai_system"]["conversion_rate"]},
            {"Metric": "Revenue per User (SAR)", "Baseline": sim_res["baseline"]["revenue_per_user"], "AI System": sim_res["ai_system"]["revenue_per_user"]}
        ])
        st.table(df_comp)
        
        # Chart
        st.subheader("📉 Revenue per User Comparison")
        chart_data = pd.DataFrame({
            "System": ["Baseline", "AI System"],
            "Revenue (SAR)": [sim_res["baseline"]["revenue_per_user"], sim_res["ai_system"]["revenue_per_user"]]
        })
        fig_rev = px.bar(chart_data, x="System", y="Revenue (SAR)", color="System", text_auto=True)
        st.plotly_chart(fig_rev, use_container_width=True)
        
        st.info("💡 **Observation:** The AI System consistently out-performs the baseline by filtering irrelevant cross-category items and prioritizing bundles with higher conversion probability and AOV lift.")
