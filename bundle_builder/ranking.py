
from bundle_builder.evaluation import (
    evaluate_relevance, 
    evaluate_utility, 
    evaluate_price_fit, 
    evaluate_diversity, 
    calculate_final_score,
    calculate_business_score,
    calculate_decision_score,
    validate_bundle,
    get_confidence_score
)
from bundle_builder.aov import estimate_aov_lift
from bundle_builder.conversion import estimate_conversion_probability

class RankingEngine:
    def __init__(self, budget=None, baby_age=None):
        self.budget = budget
        self.baby_age = baby_age

    def get_bundle_metrics(self, input_products, bundle_items):
        relevance = evaluate_relevance(bundle_items, input_products, self.baby_age)
        utility = evaluate_utility(bundle_items, input_products)
        
        # Failure Detection
        if relevance < 0.3 or utility < 0.3:
            return None
            
        metrics = {
            "relevance": relevance,
            "utility": utility,
            "price_fit": evaluate_price_fit(bundle_items, input_products, self.budget),
            "diversity": evaluate_diversity(bundle_items)
        }
        
        final_score = calculate_final_score(metrics)
        metrics["final_score"] = final_score
        
        # Business Scoring
        aov_data = estimate_aov_lift(input_products, bundle_items, utility)
        business_score, norm_aov = calculate_business_score(final_score, aov_data["raw_lift"])
        
        # Conversion Intelligence
        conv_prob = estimate_conversion_probability(input_products, bundle_items, metrics)
        
        # Smart Filter: Reject low conversion
        if conv_prob < 0.4:
            return None
            
        # Final Decision Score
        decision_score = calculate_decision_score(business_score, conv_prob)
        
        metrics.update({
            "business_score": business_score,
            "normalized_aov_lift": norm_aov,
            "aov_data": aov_data,
            "conversion_probability": conv_prob,
            "decision_score": decision_score
        })
        
        return metrics

    def validate(self, bundle_items):
        return validate_bundle(bundle_items)

    def get_confidence(self, final_score, metrics):
        return get_confidence_score(final_score, metrics)
