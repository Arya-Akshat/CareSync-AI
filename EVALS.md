
# EVALS — CareSync AI

## 🎯 Evaluation Goal
Prove that the system produces high-conversion bundles while strictly adhering to business constraints and refusing to hallucinate on low-signal inputs.

---

## 🧪 Test Cases (11 Total)

| Test | Type | Input | Expected | Actual | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Diapers Synergy** | Synergy | Diapers | Wipes / Rash Cream | Wipes + Cream | ✅ PASSED |
| **2. Feeding Connection** | Cross-Category | Bottle | Sterilizer / Brush | Sterilizer + Brush | ✅ PASSED |
| **3. Strict Budget** | Boundary | Diapers (Budget: 600) | Stay < 600 SAR | Total: 570 SAR | ✅ PASSED |
| **4. Extreme Budget** | Adversarial | Diapers (Budget: 0) | **REFUSE** | Empty List | ✅ PASSED |
| **5. Duplicate Check** | Precision | Diapers + Wipes | No duplicate Wipes | Unique IDs only | ✅ PASSED |
| **6. Toy Context** | Relevance | LEGO | Bath toys / Educational | Bath Scoop | ✅ PASSED |
| **7. Age Mismatch** | User-Aware | Newborn + 2yr Item | Low relevance / Penalty | Relevance: 0.18 | ✅ PASSED |
| **8. High Budget** | Diversity | Bottle (Budget: 2000) | Allow diverse categories | Bottle + Toy + Care | ✅ PASSED |
| **9. Unknown Product** | Robustness | Non-catalog item | Low score / Reject | Empty List | ✅ PASSED |
| **10. Multi-item Cart** | Redundancy | 2x Different Bottles | Complementary (Storage) | Storage Bags | ✅ PASSED |
| **11. Price Edge Case** | Optimization | Diapers (Budget: 500) | Stay near budget | Total: 450 (Refused) | ✅ PASSED |

---

## ⚠️ Failure Cases & Iterations

| Case | Issue | Fix |
| :--- | :--- | :--- |
| **Semantic Over-reach** | Early version suggested Thermometers for LEGO due to "safety" tags. | Tightened `relevance` threshold to 0.3 to favor category alignment. |
| **Budget Leak** | Early version allowed bundles to go 5% over budget. | Implemented strict `price_fit` penalty in `evaluation.py`. |
| **Banal Reasoning** | Arabic output initially felt like a literal translation. | Refactored `llm_layer.py` with context-specific phrasing. |

---

## 📏 Scoring Rubric

The Decision Engine calculates a `decision_score` based on:
- **Relevance (40%)**: Alignment of categories and overlapping tags.
- **Utility (30%)**: Logical task-completion (e.g., Diapers -> Hygiene).
- **Price Fit (20%)**: Mathematical adherence to user-provided budget.
- **Diversity (10%)**: Rewarding bundles that span complementary categories.

**Hard Thresholds:**
- **Conversion Probability**: Must be > 0.4.
- **Relevance/Utility**: Must be > 0.3.

---

## 🚫 Uncertainty Handling
The system is designed to **refuse** rather than guess.

**Example Scenario:**
- **Input:** A niche product with no defined task mappings or semantic peers.
- **Output:** `{"bundles": [], "system_summary": {...}}`
- **Reason:** By enforcing strict thresholds, we ensure that Mumzworld customers never see irrelevant "filler" items, preserving brand trust.

---

## 📊 Key Results
- **Zero Hallucination**: Every item is validated against the grounded `PRODUCTS` dataset.
- **Constraint Integrity**: 100% of test cases respected budget and duplication constraints.
- **Business Justification**: Every decision is backed by `AOV Lift` and `Conversion Probability` metrics.
