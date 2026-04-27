
import streamlit as st
import pandas as pd
import plotly.express as px
from bundle_builder.main import BundleBuilderAI, PRODUCTS
from bundle_builder.ab_test import ABTestSimulator
import subprocess

# --- Translations ---
TEXTS = {
    "English": {
        "title": "CareSync AI – Decision Intelligence",
        "subtitle": "Optimize for **Relevance**, **Revenue**, and **Conversion** in real-time.",
        "tab1": "🚀 Decision Dashboard",
        "tab2": "🧪 A/B Simulation Lab",
        "sidebar_config": "🛒 Input Configuration",
        "select_cart": "Select Products in Cart",
        "budget": "Budget (SAR)",
        "age": "Baby Age",
        "ages": ["Newborn", "3 months", "6 months", "12 months", "18 months", "2+ years"],
        "debug": "Enable Debug Mode",
        "lang": "Display Language",
        "generate": "Generate Optimized Bundles",
        "metrics_aov": "Avg AOV Lift",
        "metrics_conv": "Avg Conversion Prob",
        "metrics_conf": "Avg Confidence",
        "metrics_gen": "Bundles Generated",
        "chart_title": "📈 Decision Intelligence Chart",
        "reco_title": "🎯 Top Recommended Decisions",
        "bundle": "Bundle",
        "items": "Items",
        "score": "Decision Score",
        "logic": "Logic",
        "relevance": "Relevance",
        "utility": "Utility",
        "price_fit": "Price Fit",
        "diversity": "Diversity",
        "ab_title": "🧪 A/B Testing Simulation Lab",
        "ab_subtitle": "Prove the business impact of AI decisions against a rule-based baseline.",
        "sim_users": "Number of Simulated Users",
        "sim_seed": "Simulation Seed (Set for Reproducibility)",
        "run_sim": "Run A/B Simulation",
        "sim_done": "Simulation Complete!",
        "rev_uplift": "Revenue Uplift",
        "aov_uplift": "AOV Uplift",
        "conv_uplift": "Conversion Uplift",
        "comp_metrics": "📊 Comparative Metrics",
        "comp_aov": "Avg AOV (SAR)",
        "comp_conv": "Conversion Rate",
        "comp_rpu": "Revenue per User (SAR)",
        "rev_chart": "📉 Revenue per User Comparison",
        "observation": "The AI System out-performs the baseline by filtering irrelevant items and prioritizing conversion probability.",
        "no_bundles": "⚠️ No bundles generated.",
        "p_name_key": "name"
    },
    "Arabic (العربية)": {
        "title": "CareSync AI - ذكاء القرار",
        "subtitle": "تحسين **ملاءمة المنتجات**، **الإيرادات**، و**معدل التحويل** في الوقت الفعلي.",
        "tab1": "🚀 لوحة القرارات",
        "tab2": "🧪 مختبر محاكاة A/B",
        "sidebar_config": "🛒 إعدادات المدخلات",
        "select_cart": "اختر المنتجات في السلة",
        "budget": "الميزانية (ريال سعودي)",
        "age": "عمر الطفل",
        "ages": ["حديث الولادة", "3 أشهر", "6 أشهر", "12 شهرًا", "18 شهرًا", "سنتين فأكثر"],
        "debug": "تفعيل وضع التصحيح",
        "lang": "لغة العرض",
        "generate": "توليد الحزم المحسنة",
        "metrics_aov": "زيادة AOV",
        "metrics_conv": "احتمالية التحويل",
        "metrics_conf": "متوسط الثقة",
        "metrics_gen": "الحزم المولدة",
        "chart_title": "📈 مخطط ذكاء القرار",
        "reco_title": "🎯 أهم القرارات الموصى بها",
        "bundle": "حزمة",
        "items": "المنتجات",
        "score": "درجة القرار",
        "logic": "المنطق والتحليل",
        "relevance": "الملاءمة",
        "utility": "المنفعة",
        "price_fit": "توافق السعر",
        "diversity": "التنوع",
        "ab_title": "🧪 مختبر محاكاة اختبار A/B",
        "ab_subtitle": "إثبات الأثر التجاري لقرارات الذكاء الاصطناعي مقابل خط الأساس القائم على القواعد.",
        "sim_users": "عدد المستخدمين للمحاكاة",
        "sim_seed": "بذرة المحاكاة (لإعادة الإنتاج)",
        "run_sim": "تشغيل محاكاة A/B",
        "sim_done": "اكتملت المحاكاة!",
        "rev_uplift": "زيادة الإيرادات",
        "aov_uplift": "زيادة متوسط الطلب",
        "conv_uplift": "زيادة التحويل",
        "comp_metrics": "📊 المقاييس المقارنة",
        "comp_aov": "متوسط الطلب (ريال)",
        "comp_conv": "معدل التحويل",
        "comp_rpu": "الإيراد لكل مستخدم (ريال)",
        "rev_chart": "📉 مقارنة الإيرادات لكل مستخدم",
        "observation": "يتفوق نظام الذكاء الاصطناعي باستمرار من خلال تصفية العناصر غير ذات الصلة ومنح الأولوية للاحتمالية العالية.",
        "no_bundles": "⚠️ لم يتم توليد أي حزم.",
        "p_name_key": "name_ar"
    }
}

# Initialize
def get_engine(): return BundleBuilderAI()
def get_simulator(): return ABTestSimulator()
def get_git_hash():
    try: return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
    except: return "main"

engine = get_engine()
simulator = get_simulator()

st.set_page_config(page_title="CareSync AI Decision Lab", layout="wide")

# --- Sidebar ---
st.sidebar.markdown(f"**Build:** `{get_git_hash()}`")
st.sidebar.divider()
st.sidebar.header("⚙️ Settings")
lang = st.sidebar.radio("Display Language", ["English", "Arabic (العربية)"])
t = TEXTS[lang]
pk = t["p_name_key"]

# RTL Support for Arabic
if lang == "Arabic (العربية)":
    st.markdown("""
        <style>
        .main { direction: rtl; text-align: right; }
        div[data-testid="stSidebar"] { direction: rtl; }
        div[data-testid="stMetricValue"] { text-align: right; }
        label[data-testid="stWidgetLabel"] { text-align: right; width: 100%; }
        </style>
    """, unsafe_allow_html=True)

# --- Tabs ---
tab_dashboard, tab_ab_test = st.tabs([t["tab1"], t["tab2"]])

with tab_dashboard:
    st.title(t["title"])
    st.markdown(t["subtitle"])

    # --- Sidebar Inputs ---
    st.sidebar.divider()
    st.sidebar.header(t["sidebar_config"])
    
    product_options = {p[pk]: p["name"] for p in PRODUCTS}
    selected_product_localized = st.sidebar.multiselect(
        t["select_cart"],
        options=list(product_options.keys()),
        default=[PRODUCTS[0][pk]]
    )
    # Map back to internal names for processing
    selected_real_names = [product_options[name] for name in selected_product_localized]
    
    budget = st.sidebar.number_input(t["budget"], value=1000, step=100)
    baby_age = st.sidebar.selectbox(t["age"], t["ages"])
    debug_mode = st.sidebar.toggle(t["debug"], value=False)
    
    input_products = [p for p in PRODUCTS if p["name"] in selected_real_names]

    if st.sidebar.button(t["generate"], type="primary"):
        payload = {"products": input_products, "budget": budget, "baby_age": baby_age}
        with st.spinner("Analyzing..."):
            result = engine.process_request(payload)
        
        if not result["bundles"]:
            st.warning(t["no_bundles"])
        else:
            summary = result["system_summary"]
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(t["metrics_aov"], f"{summary['avg_aov_lift']}%")
            col2.metric(t["metrics_conv"], f"{int(summary['avg_conversion_probability']*100)}%")
            col3.metric(t["metrics_conf"], f"{int(summary['avg_confidence']*100)}%")
            col4.metric(t["metrics_gen"], summary['bundles_generated'])
            
            st.divider()
            st.subheader(t["chart_title"])
            plot_data = pd.DataFrame([{
                "Bundle": f"B{i+1}", "Conversion": b["conversion_probability"], 
                "AOV Lift": b["aov_lift_percent"], "Decision Score": b["decision_score"]
            } for i, b in enumerate(result["bundles"])])
            fig = px.scatter(plot_data, x="Conversion", y="AOV Lift", size="Decision Score", color="Decision Score", text="Bundle")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader(t["reco_title"])
            for i, bundle in enumerate(result["bundles"]):
                with st.container(border=True):
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"### {t['bundle']} {i+1}")
                        st.write(f"**{t['items']}:** {', '.join([p[pk] for p in bundle['items']])}")
                    with c2:
                        st.metric(t["score"], bundle["decision_score"])
                    
                    st.write("---")
                    sc1, sc2, sc3, sc4 = st.columns(4)
                    sc1.progress(bundle["debug"]["relevance"], text=f"{t['relevance']}: {round(bundle['debug']['relevance'], 2)}")
                    sc2.progress(bundle["debug"]["utility"], text=f"{t['utility']}: {round(bundle['debug']['utility'], 2)}")
                    sc3.progress(bundle["debug"]["price_fit"], text=f"{t['price_fit']}: {round(bundle['debug']['price_fit'], 2)}")
                    sc4.progress(bundle["debug"]["diversity"], text=f"{t['diversity']}: {round(bundle['debug']['diversity'], 2)}")
                    
                    with st.expander(f"💡 {t['logic']}"):
                        if lang == "English":
                            st.info(bundle['reasoning_en'])
                        else:
                            st.markdown(f'<div style="text-align: right; direction: rtl; background-color: #e8f4f8; padding: 15px; border-radius: 8px; border-right: 5px solid #00adef; color: #1f2937;">{bundle["reasoning_ar"]}</div>', unsafe_allow_html=True)

            if debug_mode:
                st.divider()
                st.json(result)

with tab_ab_test:
    st.title(t["ab_title"])
    st.markdown(t["ab_subtitle"])
    
    num_users = st.slider(t["sim_users"], 100, 1000, 500)
    sim_seed = st.number_input(t["sim_seed"], value=42, step=1)
    
    if st.button(t["run_sim"], type="primary"):
        with st.spinner("Simulating..."):
            sim_res = simulator.run_simulation(num_users, seed=sim_seed)
            
        st.success(t["sim_done"])
        
        u1, u2, u3 = st.columns(3)
        u1.metric(t["rev_uplift"], f"{sim_res['uplift']['revenue_increase']}%", delta=sim_res['uplift']['revenue_increase'])
        u2.metric(t["aov_uplift"], f"{sim_res['uplift']['aov_increase']}%", delta=sim_res['uplift']['aov_increase'])
        u3.metric(t["conv_uplift"], f"{sim_res['uplift']['conversion_increase']}%", delta=sim_res['uplift']['conversion_increase'])
        
        st.divider()
        st.subheader(t["comp_metrics"])
        df_comp = pd.DataFrame([
            {"Metric": t["comp_aov"], "Baseline": sim_res["baseline"]["avg_aov"], "AI System": sim_res["ai_system"]["avg_aov"]},
            {"Metric": t["comp_conv"], "Baseline": sim_res["baseline"]["conversion_rate"], "AI System": sim_res["ai_system"]["conversion_rate"]},
            {"Metric": t["comp_rpu"], "Baseline": sim_res["baseline"]["revenue_per_user"], "AI System": sim_res["ai_system"]["revenue_per_user"]}
        ])
        st.table(df_comp)
        
        st.subheader(t["rev_chart"])
        chart_data = pd.DataFrame({
            "System": ["Baseline", "AI System"],
            "Revenue (SAR)": [sim_res["baseline"]["revenue_per_user"], sim_res["ai_system"]["revenue_per_user"]]
        })
        fig_rev = px.bar(chart_data, x="System", y="Revenue (SAR)", color="System", text_auto=True)
        st.plotly_chart(fig_rev, use_container_width=True)
        st.info(f"💡 {t['observation']}")
