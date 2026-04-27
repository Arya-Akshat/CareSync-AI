
def estimate_aov_lift(input_products, bundle, utility_score):
    """
    Computes business impact: lift percentage and price increase.
    Adjusts lift based on the utility (synergy) of the bundle.
    """
    base_price = sum(p["price"] for p in input_products)
    bundle_price = sum(p["price"] for p in bundle)
    total_price = base_price + bundle_price
    
    # Raw lift
    raw_lift = (total_price - base_price) / base_price if base_price > 0 else 0
    
    # Utility adjustment
    lift = raw_lift
    if utility_score >= 0.8:
        lift += 0.10
    elif utility_score < 0.4:
        lift -= 0.10
        
    # Clamp between 5% and 50%
    clamped_lift = max(0.05, min(0.5, lift))
    
    return {
        "aov_lift_percent": int(clamped_lift * 100),
        "raw_lift": clamped_lift,
        "price_increase": bundle_price,
        "total_price": total_price
    }
