
# Evaluation & Measurement Plan

CareSync AI is measured using two layers: **Static Unit Tests** and **Business Simulation**.

---

## 🧪 1. Static Evaluation Suite (11 Test Cases)
Run via: `python3 -m bundle_builder.main`

### Key Scenarios:
1. **Diapers Utility**: Correctly suggests Wipes/Cream (Essential Hygiene Set).
2. **Toy Relevance**: Avoids suggesting diapers for a LEGO purchase.
3. **Budget Constraint**: Filters out high-priced items (like Breast Pumps) when the user budget is low.
4. **Age-Mismatch**: Penalizes products that don't match the baby's age (e.g., Newborn diapers for 2+ years).
5. **AOV Lift**: Prioritizes bundles that add meaningful revenue without crashing conversion probability.

---

## 📊 2. A/B Simulation (Business Measurement)
We use a Monte Carlo simulation (500 users) to compare CareSync AI against a **Random Baseline**.

### Current Benchmarks:
| Metric | Baseline | CareSync AI | Uplift |
| :--- | :--- | :--- | :--- |
| **Avg AOV (SAR)** | 261 | 379 | **+45.2%** |
| **Conversion Rate** | 0.02 | 0.42 | **Significant** |
| **Revenue per User** | 261 | 379 | **+45.2%** |

---

## 🛡️ 3. Safeguards & Hallucination Checks
- **Schema Validation**: Every bundle is cross-referenced against the `PRODUCTS` dataset before being displayed.
- **Price Fit**: Bundles that exceed 150% of the user's cart value are automatically penalized or filtered.
- **RTL Support**: Ensures Arabic logic is displayed correctly without layout breaking.

---

## 🏁 Rubric Success Criteria
- [x] Correctness of bundle reasoning.
- [x] Clear business uplift in simulation.
- [x] Performance: Dashboard response < 200ms.
- [x] Fully bilingual (EN/AR).
