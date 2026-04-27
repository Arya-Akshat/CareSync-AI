
# Bundle Builder AI – Attach Rate Optimizer
**Mumzworld AI Intern Take-Home | Track A**

### 🚀 One-Paragraph Summary
I built **Bundle Builder AI**, a Decision Intelligence Engine designed to optimize Mumzworld's Average Order Value (AOV). Unlike basic recommenders, this system uses a hybrid retrieval layer (Rules + Semantic Similarity) and a dual-pillar scoring model that balances **Business Value (AOV Lift)** with **User Acceptance (Conversion Probability)**. It justifies every recommendation with grounded, bilingual (EN/AR) reasoning and includes a simulation layer to quantitatively prove business impact.

---

### 🛠️ Setup & Run (Under 2 Minutes)
1. **Clone & Install**:
   ```bash
   # Clone the repo
   # Install dependencies
   pip install streamlit pandas plotly
   ```
2. **Launch Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```
3. **Run Validation Suite (Terminal Output)**:
   ```bash
   python3 -m bundle_builder.main
   ```

---

### 🧪 EVALS (Evaluation & Rigor)
I implemented an automated validation suite with 8 test cases across 4 failure modes.

| Test Case | Intent | Result | Why? |
| :--- | :--- | :--- | :--- |
| **TEST 1: Diapers Utility** | Basic synergy | ✅ PASSED | Correctly pairs Diapers with Wipes/Cream. |
| **TEST 4: Budget Cap** | Constraint adherence | ✅ PASSED | Rejects bundles exceeding strict limits (600 SAR). |
| **TEST 6: Low Utility** | Failure Detection | ✅ PASSED | Correctly filters out weak cross-category matches. |
| **TEST 8: Conversion Filter** | User Acceptance | ✅ PASSED | Rejects high-price/low-relevance bundles. |

**Rubric:**
- **Relevance (40%)**: Category and tag alignment.
- **Utility (30%)**: Task-completion logic (e.g., feeding bottle -> brush).
- **Price Fit (20%)**: Proximity to budget vs. AOV goals.
- **Conversion (Built-in)**: Behavioral probability filter (Threshold: 0.4).

---

### ⚖️ TRADEOFFS (Judgment & Scoping)
- **Why this problem?** I chose AOV optimization because it is a "hard" engineering problem where AI value is measurable. Most recommendation engines ignore price psychology; this system builds it into the core ranking.
- **Architecture**: I used a modular "Layered Ranking" approach (Retrieval -> Scoring -> Decision -> Simulation) rather than a single LLM call. This makes the system deterministic and explainable.
- **Uncertainty Handling**: I implemented a **Decision Filter**. If a bundle scores below 0.3 on relevance or 0.4 on conversion, the system returns an empty result rather than a "hallucinated" guess. This prevents "bad" suggestions on outlier carts.
- **What I cut**: I prioritized the Decision Intelligence logic and Simulation Layer over complex multi-modal input (image-to-bundle) to ensure the core business logic was production-ready and provable.

---

### 🤖 Tooling & AI Usage
- **Harness**: Antigravity (Gemini 2.0 Flash) for rapid architecture scaffolding and logic refinement.
- **Usage**: Full agent loops for data generation and pair-coding for the ranking formulas.
- **Provenance**: I designed the scoring weights; the AI implemented the vectorized comparisons. I overruled the agent on the Arabic translations to ensure "Native" sounding copy (e.g., using context-specific hygiene terms like "العناية اليومية المتكاملة").

---

### ⏳ Time Log
- **Phase 1 (Discovery & Scoping)**: 45m
- **Phase 2 (Core Engine & Retrieval)**: 1h 30m
- **Phase 3 (Evaluation & Simulation Layer)**: 1h 45m
- **Phase 4 (Dashboard & Documentation)**: 1h
- **Total**: ~5 hours
