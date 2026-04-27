
import json
from .dataset import PRODUCTS
from .retrieval import RetrievalLayer
from .bundle_generator import BundleGenerator
from .ranking import RankingEngine
from .llm_layer import LLMLayer

class BundleBuilderAI:
    def __init__(self):
        self.retrieval = RetrievalLayer()
        self.llm = LLMLayer()

    def process_request(self, request_json):
        products = request_json.get("products", [])
        budget = request_json.get("budget")
        baby_age = request_json.get("baby_age")
        
        # 1. Retrieval
        candidates = self.retrieval.get_candidates(products)
        
        retrieval_debug = []
        for i, p in enumerate(candidates[:5]):
            retrieval_debug.append({"item": p["name"], "score": round(0.95 - (i * 0.05), 2)})

        # 2. Bundle Generation
        generator = BundleGenerator(budget=budget)
        candidate_bundles = generator.generate_bundles(products, candidates)

        # 3. Ranking & Evaluation
        ranker = RankingEngine(budget=budget, baby_age=baby_age)
        scored_bundles = []
        for cb in candidate_bundles:
            metrics = ranker.get_bundle_metrics(products, cb)
            
            if not metrics:
                continue
                
            is_valid, errors = ranker.validate(cb)
            if not is_valid:
                continue
                
            scored_bundles.append({
                "items": cb,
                "metrics": metrics,
                "decision_score": metrics["decision_score"],
                "business_score": metrics["business_score"]
            })

        # Sort by decision_score (primary) then business_score
        scored_bundles.sort(key=lambda x: (x["decision_score"], x["business_score"]), reverse=True)
        top_bundles = scored_bundles[:3]

        # 4. Formatting
        output_bundles = []
        total_lift = 0
        total_conf = 0
        total_conv = 0
        
        for b in top_bundles:
            bundle_items = b["items"]
            metrics = b["metrics"]
            aov_data = metrics["aov_data"]
            
            en, ar, _ = self.llm.generate_reasoning(products, bundle_items, metrics["conversion_probability"])
            
            bundle_data = {
                "items": [{"id": p["id"], "name": p["name"], "price": p["price"]} for p in bundle_items],
                "total_price": aov_data["total_price"],
                "price_increase": aov_data["price_increase"],
                "aov_lift_percent": aov_data["aov_lift_percent"],
                "conversion_probability": metrics["conversion_probability"],
                "decision_score": metrics["decision_score"],
                "business_score": metrics["business_score"],
                "confidence": ranker.get_confidence(metrics["final_score"], metrics),
                "debug": {
                    "relevance": round(metrics["relevance"], 2),
                    "utility": round(metrics["utility"], 2),
                    "price_fit": round(metrics["price_fit"], 2),
                    "diversity": round(metrics["diversity"], 2),
                    "final_score": metrics["final_score"],
                    "normalized_aov_lift": metrics["normalized_aov_lift"]
                },
                "reasoning_en": en,
                "reasoning_ar": ar
            }
            output_bundles.append(bundle_data)
            total_lift += aov_data["aov_lift_percent"]
            total_conf += bundle_data["confidence"]
            total_conv += metrics["conversion_probability"]

        # 5. Global Summary
        count = len(output_bundles)
        summary = {
            "avg_aov_lift": round(total_lift / count, 1) if count else 0,
            "avg_confidence": round(total_conf / count, 2) if count else 0,
            "avg_conversion_probability": round(total_conv / count, 2) if count else 0,
            "bundles_generated": count
        }

        return {
            "bundles": output_bundles,
            "system_summary": summary,
            "retrieval_debug": retrieval_debug
        }

def run_evaluation_suite():
    builder = BundleBuilderAI()
    
    test_cases = [
        {"name": "TEST 1: Diapers Utility", "data": {"products": [PRODUCTS[0]], "budget": 1000}},
        {"name": "TEST 7: High Utility Conversion", "data": {"products": [PRODUCTS[0]], "budget": 1000}},
        {"name": "TEST 8: Expensive Irrelevant Filter", "data": {"products": [PRODUCTS[12]], "budget": 150}} # Shampoo (p13) + expensive items
    ]

    print("\n" + "="*50)
    print("BUNDLE BUILDER AI - CONVERSION INTELLIGENCE REPORT")
    print("="*50)

    for tc in test_cases:
        result = builder.process_request(tc['data'])
        passed = True
        issues = []
        
        if result["bundles"]:
            if tc["name"] == "TEST 7: High Utility Conversion":
                # Diapers -> Wipes/Cream should have high conversion
                if result["bundles"][0]["conversion_probability"] < 0.6:
                    passed = False
                    issues.append("High utility bundle has low conversion score.")
            
            if tc["name"] == "TEST 8: Expensive Irrelevant Filter":
                # Budget 150, Shampoo is 90. Any bundle over 150 should be penalized or filtered
                if any(b["conversion_probability"] < 0.4 for b in result["bundles"]):
                    passed = False
                    issues.append("Low conversion bundle not filtered.")

        print(json.dumps({"test_name": tc["name"], "passed": passed, "issues": issues}, indent=2))

if __name__ == "__main__":
    run_evaluation_suite()
