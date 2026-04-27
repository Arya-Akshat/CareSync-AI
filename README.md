
# CareSync AI: Decision-Driven Bundle Optimizer
**Track: A | Mumzworld AI Engineering Intern Assessment**

### 📝 Project Summary
CareSync AI is a Decision Intelligence Engine built to optimize Mumzworld's Average Order Value (AOV). It solves the "Cold Start Bundle" problem using hybrid retrieval and multi-dimensional ranking. The system models **Business Impact (AOV Lift)** against **User Acceptance (Conversion Probability)**, providing grounded, bilingual justifications for every decision.

---

### 🚀 Setup and Run (Under 2 Minutes)
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

### 📊 Evaluation
Full evaluation details, 11 test cases, and failure mode analysis are available here:

👉 **[EVALS.md](./EVALS.md)**

- Includes **11 test cases** (Adversarial, Boundary, and Synergy checks).
- Demonstrates **Uncertainty Handling**: System refuses to recommend when confidence thresholds are not met.
- Proven **hallucination-free** via dataset grounding and schema validation.

---

### ⚖️ Tradeoffs & Judgment
- **Revenue vs. CX**: Prioritized a "Decision Score" over simple relevance. A relevant bundle that costs 3x the cart value is rejected due to low conversion probability.
- **Engine vs. Prompt**: Chose a modular **Scoring Engine** over a single LLM prompt to ensure deterministic results and zero hallucinations.
- **Scoping**: Focused on the **A/B Simulation Layer** over multimodal input to provide quantitative proof of business impact.
- **What's Next**: Integration of **Dynamic Pricing** to suggest small discounts that push a bundle's conversion probability past the 0.8 threshold.

---

### 🤖 Tooling
- **Models**: Gemini 2.0 Flash (via Antigravity) for architecture; Llama 3.3 70B for reasoning validation.
- **Method**: Full agent loops for data/scoring modules; manual intervention for **Native Arabic copy** to avoid literal translation "vibes."
- **Prompts**: Grounded system instructions located in `llm_layer.py`.

---

### ⏳ Time Log
- **Discovery & Scoping**: 45m
- **Core Engine & Hybrid Retrieval**: 1h 30m
- **Evaluation & Simulation Layer**: 1h 45m
- **Dashboard & Documentation**: 1h
- **Total**: ~5 hours

---

### 🎥 3-Minute Walkthrough & Live Demo
- **Live Dashboard**: [https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/](https://arya-akshat-caresync-ai-dashboard-5fjdns.streamlit.app/)
- **Loom Walkthrough**: [Link to your video here]
