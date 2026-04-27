
def estimate_conversion_probability(input_products, bundle, metrics):
    """
    Estimates the likelihood of a user accepting the bundle.
    Considers price increase ratios and product synergy.
    """
    relevance = metrics.get("relevance", 0)
    utility = metrics.get("utility", 0)
    price_fit = metrics.get("price_fit", 0)
    
    # Base score (Relevance is king for acceptance)
    conversion = (0.7 * relevance) + (0.2 * utility) + (0.1 * price_fit)
    
    # Low quality penalty (Crucial for Baseline differentiation)
    # If a bundle is random junk, it should have near-zero conversion
    if relevance < 0.2 and utility < 0.2:
        conversion -= 0.4
    
    # Price ratio analysis
    base_price = sum(p["price"] for p in input_products)
    bundle_price = sum(p["price"] for p in bundle)
    
    if base_price > 0:
        price_ratio = bundle_price / base_price
        if price_ratio > 0.5:
            conversion -= 0.15
            
    # Size penalty
    if len(bundle) > 3:
        conversion -= 0.1
        
    # Synergy boosts
    if utility >= 0.8:
        conversion += 0.2
        
    # Strong category match boost
    input_cats = {p["category"] for p in input_products}
    if any(p["category"] in input_cats for p in bundle):
        conversion += 0.05
        
    return round(max(0.05, min(1.0, conversion)), 2) # 5% floor for "dumb luck"
