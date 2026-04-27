
def estimate_conversion_probability(input_products, bundle, metrics):
    """
    Estimates the likelihood of a user accepting the bundle.
    Considers price increase ratios and product synergy.
    """
    relevance = metrics.get("relevance", 0)
    utility = metrics.get("utility", 0)
    price_fit = metrics.get("price_fit", 0)
    
    # Base score
    conversion = (0.6 * relevance) + (0.3 * utility) + (0.1 * price_fit)
    
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
        
    return round(max(0.0, min(1.0, conversion)), 2)
