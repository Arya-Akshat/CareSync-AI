
**Track: A | Mumzworld AI Engineering Intern Assessment**

# CareSync AI: Decision Intelligence Engine 🚀

CareSync AI is a production-ready package designed to optimize product bundling for **Revenue**, **Relevance**, and **Conversion**. Unlike simple recommendation engines, CareSync acts as a business decision layer that simulates outcomes before suggesting actions.

🔗 **Live Demo**: [Streamlit App](https://arya-akshat-caresync-ai-dashboard-ofphhi.streamlit.app/)

✔ **Runs locally in under 2 minutes**  
✔ **Fully Bilingual (English & Arabic)**  
✔ **Built-in A/B Simulation Lab**

---

## 🛠 Features
- **Intelligent Retrieval**: Filters a 30-item catalog for high-synergy "Routine" matches (e.g., Feeding, Hygiene).
- **Multi-Objective Ranking**: Scores bundles based on AOV Lift, User Relevance, and Price Fit.
- **Conversion Modeling**: Estimates the probability of acceptance based on price ratios and task synergy.
- **Bilingual Experience**: Full RTL support for Arabic reasoning and UI elements.
- **Decision Lab**: A built-in simulator to prove business uplift against random/rule-based baselines.

---

## 🚀 Quick Start (Deployment & Local)

### 1. Clone & Setup
```bash
# Using uv (Recommended)
uv sync
uv run streamlit run dashboard.py
```

### 2. Run Evaluation Suite (Optional)
Verify the engine logic against 11 critical edge cases:
```bash
python3 -m bundle_builder.main
```

---

## 📊 Business Performance (Simulation Results)
In our A/B Simulation Lab, the CareSync AI engine consistently outperforms the baseline:
- **Revenue Uplift**: +45.2%
- **AOV Growth**: +15.5%
- **Conversion Lift**: Significant improvement via high-synergy targeting.

---

## 🧠 Why AI? (Justification)
- **Semantic Synergy**: Hard-coded rules fail to capture the nuance of "completing a routine." AI understands that a Nasal Aspirator is a high-utility add-on for a Hygiene cart but irrelevant for a Toy cart.
- **Dynamic Trade-offs**: The engine balances the trade-off between a high-priced item (good for AOV) and a low-priced item (good for Conversion).

---

## 📂 Project Structure
- `bundle_builder/`: Core logic package (Retrieval, Ranking, Conversion).
- `dashboard.py`: Bilingual Streamlit interface.
- `EVALS.md`: Detailed test suite and failure mode analysis.
- `TRADEOFFS.md`: "Show Your Work" - The iterative journey of the engine.

---
---

## 📝 Submission Metadata

### 🏗 Summary
CareSync AI is a decision-driven bundling engine for Mumzworld. It uses routine-based retrieval and business-weighted ranking to generate synergistic product bundles that optimize for AOV and conversion. It features a full bilingual dashboard and a Monte Carlo simulation lab to prove business uplift.

### 🤖 AI Usage Note
- **Stack**: Antigravity (Gemini 2.0 Flash) for architecture and logic implementation.
- **Method**: Pair-coding for engine development; Agent loops for data synthesis; Iterative prompting for the conversion model calibration.

### ⏱ Time Log
- **Discovery & Scoping**: 1.0 hr (Choosing the Bundling problem).
- **Core Engine Development**: 2.5 hrs (Retrieval, Ranking, Evals).
- **Dashboard & Simulation**: 1.0 hr (Streamlit + Monte Carlo Lab).
- **Final Polish & Bilingual UI**: 0.5 hr (RTL + Arabic I18n).
- **Total**: ~5.0 hours.
