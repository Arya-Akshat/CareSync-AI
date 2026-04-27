
**Track: A | Mumzworld AI Engineering Intern Assessment**

# CareSync AI: Decision Intelligence Engine 🚀

CareSync AI is a production-ready package designed to optimize product bundling for **Revenue**, **Relevance**, and **Conversion**. Unlike simple recommendation engines, CareSync acts as a business decision layer that simulates outcomes before suggesting actions.

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
- `PROCESS.md`: "Show Your Work" - The iterative journey of the engine.

---
**Build Traceability**: Current Build ID visible in the dashboard sidebar.
