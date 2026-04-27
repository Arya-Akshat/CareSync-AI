
# CareSync AI: Decision-Driven Bundle Optimizer

CareSync AI is an **Attach Rate Optimizer** designed for modern e-commerce. It solves the "Cold Start Bundle" problem by using a Decision Intelligence Engine to suggest product combinations that balance **customer relevance** with **business revenue**.

---

## 🎯 What is this project?
Most recommendation engines just look for "similar" items. CareSync AI goes further by acting as a **Decision Engine**. It evaluates every possible bundle across three critical pillars:
1.  **Relevance**: Do these items actually belong together?
2.  **Revenue (AOV Lift)**: How much does this increase the average order value?
3.  **Acceptance (Conversion %)**: How likely is the user to actually buy this?

---

## 🖥️ Dashboard Walkthrough
The included **Streamlit Dashboard** is divided into two main labs:

### 1. Decision Dashboard (The User Interface)
*   **Input**: Select items from the catalog (e.g., Diapers, Baby Bottles) and set a budget.
*   **Generation**: When you click **"Generate Optimized Bundles"**, the engine retrieves complementary candidates from the database.
*   **Ranking**: The system ranks bundles using a **Decision Score**. You see ranked cards showing the **AOV Lift**, **Conversion Probability**, and **Bilingual Reasoning** (English & Arabic) justifying the choice.

### 2. A/B Simulation Lab (The Business Proof)
*   **The Goal**: Quantitatively prove that the AI-driven approach beats traditional rule-based baselines.
*   **The Simulation**: This tab simulates hundreds of "synthetic shopping journeys." It pits a **Baseline (Random/Rule-only)** system against the **CareSync AI**.
*   **The Result**: It calculates metrics like **Revenue per User** and **Conversion Uplift**, demonstrating exactly how the Decision Engine filters out weak recommendations to maximize ROI.

---

## 🚀 Setup and Run (Under 2 Minutes)
1. **Clone and Install**:
   ```bash
   pip install streamlit pandas plotly
   ```
2. **Launch Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```
3. **Run Validation Suite**:
   ```bash
   python3 -m bundle_builder.main
   ```

---

## 📊 Evaluation & Rigor
Full evaluation details, 11 test cases, and failure analysis are available here:
👉 **[EVALS.md](./EVALS.md)**

*   **Uncertainty Handling**: If the system cannot find a high-confidence bundle, it **refuses** to recommend (preventing user friction).
*   **Hallucination-Free**: Every item is grounded in a physical dataset; no "fake" products are ever generated.

---

## ⚖️ Tradeoffs & Judgment
- **Revenue vs. CX**: Chose to reject high-margin bundles if their **Conversion Probability** is too low, prioritizing long-term customer trust.
- **Engine vs. Prompt**: Built a modular scoring engine over a single "GPT prompt" to ensure deterministic results and zero hallucinations.
- **Cuts from Scope**: Prioritized the **A/B Simulation Layer** over multimodal input to provide quantitative proof of business impact.

---

## 🤖 Tooling & AI Usage
- **Harness**: Antigravity (Gemini 2.0 Flash) for architecture; Llama 3.3 70B for reasoning validation.
- **Method**: Full agent loops for data/scoring modules; manual intervention for **Native Arabic copy** to avoid literal translation "vibes."

---

## ⏳ Time Log
- **Discovery & Core Engine**: 2h 15m
- **Evaluation & Simulation**: 1h 45m
- **Dashboard & Documentation**: 1h
- **Total**: ~5 hours

---

### 🎥 Walkthrough & Live Demo
- **Live Dashboard**: [https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/](https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/)
- **Loom Walkthrough**: [Link to your video here]
