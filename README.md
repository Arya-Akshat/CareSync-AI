
# CareSync AI: Decision-Driven Bundle Optimizer
**Track: A | Mumzworld AI Engineering Intern Assessment**

CareSync AI is an **Attach Rate Optimizer** that solves the "Cold Start Bundle" problem for e-commerce. It uses a Decision Intelligence Engine to balance **customer relevance** with **business revenue**.

---

## 📂 Documentation
- **Technical Evaluation**: [EVALS.md](./EVALS.md) (11 Test Cases & Proof of Correctness)
- **Process & Iteration**: [PROCESS.md](./PROCESS.md) (Prompts, Dead Ends, & "Show Your Work")

---

## 🧠 Why AI? (Justification)
Unlike traditional rules-based systems, CareSync AI handles:
- **Semantic Nuance**: It understands that a "Sterilizer" and a "Bottle" have a functional relationship that simple category matching misses.
- **Dynamic Tradeoffs**: It calculates the mathematical "sweet spot" between a high AOV (Revenue) and a high Conversion Probability (User Friction).
- **Native Context**: It generates grounded, bilingual reasoning that explains *why* a bundle matters, which static merchandising cannot do.

---

## 🛠️ Architecture & Flow
1. **Retrieval**: Hybrid logic (Hard Rules + Jaccard Similarity) identifies candidates from the grounded `PRODUCTS` dataset.
2. **Ranking**: The **Scoring Engine** evaluates candidates across 4 dimensions: Relevance, Utility, Price Fit, and Diversity.
3. **Decision Intelligence**: Calculates `AOV Lift` and `Conversion Probability`. Bundles below a **0.4 conversion threshold** are automatically rejected.
4. **Bilingual Reasoning**: The LLM Layer generates native English and Arabic justifications for the final selection.

---

## 🖥️ Dashboard Walkthrough
The included **Streamlit Dashboard** features:
1. **The Decision Lab**: Select items, click **"Generate Optimized Bundles"**, and see ranked cards with **AOV Lift** and **Confidence scores**.
2. **A/B Simulation Lab**: Simulates 500+ shopping journeys to prove that the AI-driven approach outperforms simple rule-based baselines in total revenue generated.

---

## 🚫 Uncertainty Handling (Example)
The system is built to refuse rather than guess.
- **Input**: *Baby Shampoo* with a **0 SAR Budget**.
- **System Output**: `[]` (Empty List).
- **Reason**: The engine enforces a hard `price_fit` and `confidence` threshold. If no synergistic item fits the budget, it returns no recommendation to maintain user trust.

---

## 📈 Measurement & Rollout (Experiment Design)
- **Leading Metric**: **Revenue per User (RPU)** — the ultimate measure of AOV × Conversion.
- **Rollout Plan**: A 5% "Canary" rollout on the product detail page (PDP) compared against the legacy "Customers Also Bought" baseline.
- **Success Criteria**: A sustained **>15% uplift in RPU** over 7 days with no increase in cart abandonment.

---

## ⚠️ Limitations
- **Dataset Grounding**: Current logic is limited to the provided 30-item catalog.
- **Heuristic Conversion**: Acceptance likelihood is modeled based on price-to-base ratios, not yet on real-time user clickstream data.

---

## 🚀 Setup and Run (Under 2 Minutes)
1. **Install Dependencies**:
   ```bash
   pip install streamlit pandas plotly
   ```
2. **Launch Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

---

## ⏳ Time Log & Tooling
- **Total Time**: 5 hours (Discovery: 1h, Logic: 2.5h, UI/Docs: 1.5h)
- **Harness**: Antigravity (Gemini 2.0 Flash) & Llama 3.3 70B for logic/reasoning.
- **Method**: Full agent loops for scoring modules; manual intervention for Native Arabic context.

---

### 🎥 Walkthrough & Live Demo
- **Live Dashboard**: [https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/](https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/)
- **Loom Walkthrough**: [Link to your video here]
