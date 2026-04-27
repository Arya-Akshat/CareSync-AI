
from bundle_builder.dataset import PRODUCTS

def evaluate_relevance(bundle, input_products, baby_age=None):
    """Score 0-1 based on category alignment and tag overlap."""
    if not bundle or not input_products:
        return 0.0
    
    input_categories = {p["category"] for p in input_products}
    input_tags = set()
    for p in input_products:
        input_tags.update(p["tags"])
        
    scores = []
    for item in bundle:
        item_score = 0
        if item["category"] in input_categories:
            item_score += 0.6
        
        tag_overlap = set(item["tags"]) & input_tags
        item_score += 0.4 * (len(tag_overlap) / max(1, len(item["tags"])))
        
        # User-Aware: Baby Age Boost
        if baby_age:
            age_tags = [t.lower() for t in item["tags"]]
            if baby_age.lower() in age_tags or ("months" in baby_age and "infant" in age_tags):
                item_score += 0.1
                
        scores.append(min(item_score, 1.0))
        
    return sum(scores) / len(scores)

def evaluate_utility(bundle, input_products):
    """Score 0-1: Does the bundle complete a real-world task?"""
    task_map = {
        "diapers": ["wipes", "rash_cream", "powder"],
        "bottle": ["sterilizer", "brush", "anti-colic"],
        "bath": ["scoop", "shampoo", "teether"]
    }
    
    score = 0
    input_tags = set()
    for p in input_products:
        input_tags.update(p["tags"])
        
    for tag in input_tags:
        if tag in task_map:
            targets = task_map[tag]
            for item in bundle:
                if any(t in item["tags"] for t in targets):
                    score += 0.5
                    
    return min(score, 1.0)

def evaluate_price_fit(bundle, input_products, budget):
    """Score 0-1: 1 if within budget, penalized more if budget is tight."""
    if not budget:
        return 1.0
    
    base_price = sum(p["price"] for p in input_products)
    total_price = base_price + sum(p["price"] for p in bundle)
    
    if total_price <= budget:
        return 1.0
    
    # Aggressive tight-budget penalty
    tightness = base_price / budget
    penalty_factor = 0.2 if tightness < 0.8 else 0.1 # Smaller range for failure if budget is tight
    
    penalty = (total_price - budget) / (budget * penalty_factor)
    return max(0.0, 1.0 - penalty)

def evaluate_diversity(bundle):
    """Score 0-1: Different but complementary categories."""
    if len(bundle) <= 1:
        return 1.0
    categories = {item["category"] for item in bundle}
    return len(categories) / len(bundle)

def calculate_final_score(metrics):
    """Weighted sum of metrics."""
    score = (0.4 * metrics["relevance"] + 
             0.3 * metrics["utility"] + 
             0.2 * metrics["price_fit"] + 
             0.1 * metrics["diversity"])
    return round(score, 2)

def calculate_business_score(final_score, lift_raw):
    """Business Score = 60% system quality + 40% revenue impact."""
    normalized_aov_lift = min(1, lift_raw / 0.5)
    score = (0.6 * final_score) + (0.4 * normalized_aov_lift)
    return round(score, 2), round(normalized_aov_lift, 2)

def calculate_decision_score(business_score, conversion_prob):
    """Balanced Decision Score: Impact vs Acceptance."""
    score = (0.5 * business_score) + (0.5 * conversion_prob)
    return round(score, 2)

def validate_bundle(bundle):
    """Hallucination Check: Ensure items exist in dataset and are valid."""
    product_ids = {p["id"] for p in PRODUCTS}
    errors = []
    seen_ids = set()
    for item in bundle:
        if item["id"] not in product_ids:
            errors.append(f"Hallucination: {item['id']}")
        if item["id"] in seen_ids:
            errors.append(f"Duplicate: {item['id']}")
        seen_ids.add(item["id"])
    return len(errors) == 0, errors

def get_confidence_score(final_score, metrics):
    conf = final_score
    if metrics["relevance"] < 0.3: conf -= 0.1
    if metrics["price_fit"] < 1.0: conf -= 0.1
    return max(0.0, min(1.0, round(conf, 2)))
