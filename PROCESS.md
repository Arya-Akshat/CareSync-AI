
# Process & Iteration — CareSync AI

This document satisfies the **"Show Your Work"** requirement, revealing the technical evolution and human-in-the-loop decisions made during the 5-hour build.

## 🛠️ Prompts that Mattered
I used a "Grounding-First" prompting strategy to ensure the LLM reasoning never hallucinated product features.

### Prompt 1: The Synergy Scorer (Iteration 2)
> **Prompt:** "Analyze the following bundle: [Items]. Check for 'Task Synergy' (do these items complete a specific job like feeding or hygiene?). Use only the provided tags. If the synergy is weak, return a 'Uncertainty' flag."
> **Why it changed:** The first version didn't have the 'Uncertainty' flag, causing the model to invent reasons for irrelevant pairings. Adding this flag enabled the **Refusal Logic** that is core to the final engine.

### Prompt 2: Native GCC Arabic Context
> **Prompt:** "Translate this reasoning to Arabic. Avoid 'Standard Classroom Arabic.' Use the tone of a premium GCC retailer (e.g., Mumzworld). Use terms like 'العناية اليومية' (daily care) instead of literal translations of 'hygiene items'."
> **Why it changed:** Literal translations felt "robotic." This prompt shift ensured the output felt like native copy.

---

## 🚧 Dead Ends & Lessons Learned
1. **Semantic Embeddings for Small Datasets**: 
   - *Dead End:* Initially tried using deep semantic embeddings to find "similar" products.
   - *Lesson:* With a 30-item dataset, embeddings are overkill and often lack "Retail Common Sense" (e.g., a diaper and a toy are both 'baby products' but have zero synergy). I switched to **Hybrid Retrieval** (Hard Rules + Jaccard Similarity) which is more interpretable and controllable.
2. **The "Greedy" Revenue Model**: 
   - *Dead End:* My early ranking engine prioritized the highest price items to maximize AOV.
   - *Lesson:* This led to extremely low **Conversion Probability**. I refactored the engine to penalize bundles that increased the cart value by >50%, realizing that a $10 sale that happens is better than a $100 recommendation that is ignored.
3. **The Budget "Leak"**:
   - *Dead End:* Allowed the AI to "suggest" items slightly over budget if they were a perfect match.
   - *Lesson:* Customers view budgets as hard filters. I refactored `price_fit` to be a binary disqualifier for any item exceeding the limit.

---

## 🧠 Key Decisions
- **Decision 1: Modular Logic over "Prompt Magic"**: I decided to code the scoring logic in Python (`evaluation.py`) rather than asking the LLM to "score" the bundle. This ensures the results are deterministic and reproducible.
- **Decision 2: Rebranding to CareSync**: To move from a "recommender" to a "service," I branded the engine as **CareSync**, emphasizing the harmony (Sync) of the care routine.
- **Decision 3: The Refusal Threshold**: I set a hard threshold of **0.3**. If no bundle reaches this, the system returns an empty list. This "Honest AI" approach builds more trust than a "Guessing AI."
