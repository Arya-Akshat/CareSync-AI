
import itertools
import random

class BundleGenerator:
    def __init__(self, budget=None):
        self.budget = budget

    def generate_bundles(self, input_products, candidates, count=5):
        bundles = []
        
        # We want to create bundles of 1-2 candidates to add to the input
        # To make it more interesting, we'll try combinations of candidates
        
        # Try pairs of candidates
        pairs = list(itertools.combinations(candidates, 2))
        random.shuffle(pairs)
        
        for pair in pairs:
            bundle_items = list(pair)
            total_price = sum(p["price"] for p in bundle_items)
            
            # Check budget if it's a constraint on the ADDED items or total?
            # Usually budget is for the total cart. 
            input_price = sum(p["price"] for p in input_products)
            if self.budget and (input_price + total_price) > self.budget:
                continue
                
            bundles.append(bundle_items)
            if len(bundles) >= count:
                break
                
        # If not enough bundles, try single items
        if len(bundles) < count:
            for cand in candidates:
                if [cand] not in bundles:
                    total_price = cand["price"]
                    input_price = sum(p["price"] for p in input_products)
                    if self.budget and (input_price + total_price) > self.budget:
                        continue
                    bundles.append([cand])
                    if len(bundles) >= count:
                        break
                        
        return bundles
