
import random
from bundle_builder.main import BundleBuilderAI, PRODUCTS
from bundle_builder.evaluation import evaluate_relevance, evaluate_utility, evaluate_price_fit
from bundle_builder.conversion import estimate_conversion_probability

class ABTestSimulator:
    def __init__(self, seed=42):
        self.ai_system = BundleBuilderAI()
        random.seed(seed)

    def get_baseline_bundle(self, input_products, budget):
        """Baseline: Simple random bundle from candidates."""
        candidates = [p for p in PRODUCTS if p not in input_products]
        bundle = random.sample(candidates, k=min(2, len(candidates)))
        
        # Calculate metrics for baseline (needed for simulation)
        metrics = {
            "relevance": evaluate_relevance(bundle, input_products),
            "utility": evaluate_utility(bundle, input_products),
            "price_fit": evaluate_price_fit(bundle, input_products, budget),
            "diversity": 1.0
        }
        conv_prob = estimate_conversion_probability(input_products, bundle, metrics)
        
        return {
            "items": bundle,
            "total_price": sum(p["price"] for p in input_products) + sum(p["price"] for p in bundle),
            "conversion_probability": conv_prob
        }

    def run_simulation(self, num_users=100):
        baseline_stats = {"revenue": 0, "conversions": 0, "total_aov": 0}
        ai_stats = {"revenue": 0, "conversions": 0, "total_aov": 0}

        for _ in range(num_users):
            # 1. Setup random scenario
            input_prod = [random.choice(PRODUCTS)]
            budget = random.randint(500, 2000)
            base_price = input_prod[0]["price"]

            # 2. Get Baseline Simulation
            base_bundle = self.get_baseline_bundle(input_prod, budget)
            if random.random() < base_bundle["conversion_probability"]:
                baseline_stats["conversions"] += 1
                baseline_stats["revenue"] += base_bundle["total_price"]
                baseline_stats["total_aov"] += base_bundle["total_price"]
            else:
                baseline_stats["revenue"] += base_price
                baseline_stats["total_aov"] += base_price

            # 3. Get AI Simulation
            ai_result = self.ai_system.process_request({"products": input_prod, "budget": budget})
            if ai_result["bundles"]:
                top_ai = ai_result["bundles"][0]
                if random.random() < top_ai["conversion_probability"]:
                    ai_stats["conversions"] += 1
                    ai_stats["revenue"] += top_ai["total_price"]
                    ai_stats["total_aov"] += top_ai["total_price"]
                else:
                    ai_stats["revenue"] += base_price
                    ai_stats["total_aov"] += base_price
            else:
                ai_stats["revenue"] += base_price
                ai_stats["total_aov"] += base_price

        # 4. Aggregation
        res = {
            "baseline": {
                "avg_aov": int(baseline_stats["total_aov"] / num_users),
                "conversion_rate": round(baseline_stats["conversions"] / num_users, 2),
                "revenue_per_user": int(baseline_stats["revenue"] / num_users)
            },
            "ai_system": {
                "avg_aov": int(ai_stats["total_aov"] / num_users),
                "conversion_rate": round(ai_stats["conversions"] / num_users, 2),
                "revenue_per_user": int(ai_stats["revenue"] / num_users)
            }
        }
        
        res["uplift"] = {
            "aov_increase": round(((res["ai_system"]["avg_aov"] / res["baseline"]["avg_aov"]) - 1) * 100, 1),
            "conversion_increase": round(((res["ai_system"]["conversion_rate"] / res["baseline"]["conversion_rate"]) - 1) * 100, 1) if res["baseline"]["conversion_rate"] > 0 else 0,
            "revenue_increase": round(((res["ai_system"]["revenue_per_user"] / res["baseline"]["revenue_per_user"]) - 1) * 100, 1)
        }
        
        return res
