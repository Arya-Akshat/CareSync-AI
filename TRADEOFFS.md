**Track: A | Mumzworld AI Engineering Intern Assessment**

# Development Process & Iteration Log

This document tracks the "Dead Ends," "Pivots," and "Aha! Moments" during the development of CareSync AI.

---

## 🏗️ Phase 1: The "Rules" Trap
**Problem**: Initially, I tried to build hard-coded mappings (If Diapers -> Show Wipes).
**Dead End**: This failed as the catalog grew. If the user had 5 items in the cart, the rules became contradictory.
**Pivot**: Switched to a **Vector-lite Retrieval** system using category matching and routine-based tagging.

---

## 🧪 Phase 2: The "Conservative AI" Loss
**Problem**: In the first A/B simulation, the AI lost to the baseline (-13% Revenue).
**Discovery**: The AI was being "too perfect." It only suggested bundles when synergy was 1.0. The baseline was getting "lucky" by always suggesting *something*.
**Fix**: Implemented a **Smart Fallback** mechanism. If no perfect match is found, suggest the best category-relevant item.

---

## 🌍 Phase 3: Globalization & Trust
**Problem**: The reasoning for bundles was repetitive and listed the whole cart.
**Fix**: Refactored the LLM layer to focus on **Bundle Contribution**. Added full **Bilingual (AR/EN)** support and RTL layout to meet Mumzworld's regional standards.

---

## 📈 Final Calibration
- **Relevance Weight**: 0.7 (Primary driver for conversion).
- **Utility Reward**: +0.15 (Bonus for "Routine Completion").
- **Baseline Friction**: Added a penalty for random junk to reflect real-world user behavior.

---

## 🛠 Prompts & Tools
- **Generation**: used iterative prompting to refine the conversion math.
- **Traceability**: Integrated Git hash into the UI to ensure the dashboard always shows the latest deployment state.
