
def estimate_conversion_probability(input_products, bundle, metrics):
    """
    Estimates the likelihood of a user accepting the bundle.
    Considers price increase ratios and product synergy.
    """
    relevance = metrics.get("relevance", 0)
    utility = metrics.get("utility", 0)
    price_fit = metrics.get("price_fit", 0)
    
    # Base score (Standard Logistic Weighting)
    conversion = (0.5 * relevance) + (0.3 * utility) + (0.2 * price_fit)
    
    # Price ratio analysis
    base_price = sum(p["price"] for p in input_products)
    bundle_price = sum(p["price"] for p in bundle)
    
    if base_price > 0:
        price_ratio = bundle_price / base_price
        # Gradual penalty for price increase
        if price_ratio > 0.4:
            conversion -= 0.1
        if price_ratio > 0.8:
            conversion -= 0.2
            
    # Synergy boosts (Conservative but meaningful)
    if utility >= 0.8:
        conversion += 0.15
        
    # High-Relevance Reward
    if relevance >= 0.8:
        conversion += 0.1
        
    return round(max(0.1, min(1.0, conversion)), 2) # Realistic 10% floor for any retail offer
