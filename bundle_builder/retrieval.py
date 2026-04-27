
from .dataset import PRODUCTS

# Rule-based mapping
RULE_MAPPING = {
    "diapers": ["wipes", "rash_cream", "powder"],
    "bottle": ["sterilizer", "brush", "anti-colic"],
    "wipes": ["diapers", "rash_cream"],
    "toy": ["sensory", "educational", "bath"],
    "health": ["monitoring", "safety", "cleaning"]
}

class RetrievalLayer:
    def __init__(self):
        self.products = PRODUCTS
        # Simple rule-based booster
        self.tag_to_products = {}
        for p in self.products:
            for tag in p["tags"]:
                if tag not in self.tag_to_products:
                    self.tag_to_products[tag] = []
                self.tag_to_products[tag].append(p)

    def _get_rule_candidates(self, input_products):
        candidates = []
        for product in input_products:
            tags = product.get("tags", [])
            for tag in tags:
                if tag in RULE_MAPPING:
                    target_tags = RULE_MAPPING[tag]
                    for ttag in target_tags:
                        candidates.extend(self.tag_to_products.get(ttag, []))
        return candidates

    def _get_semantic_candidates(self, input_products, top_n=10):
        # Lightweight embedding: Jaccard similarity on tags and description keywords
        # In a real scenario, use sentence-transformers
        scores = []
        input_texts = [p["name"] + " " + " ".join(p["tags"]) + " " + p["description"] for p in input_products]
        input_text = " ".join(input_texts).lower()
        
        for p in self.products:
            # Skip if already in input
            if any(ip["id"] == p["id"] for ip in input_products):
                continue
                
            p_text = (p["name"] + " " + " ".join(p["tags"]) + " " + p["description"]).lower()
            
            # Simple overlap score
            intersect = set(input_text.split()) & set(p_text.split())
            union = set(input_text.split()) | set(p_text.split())
            score = len(intersect) / len(union) if union else 0
            scores.append((p, score))
            
        scores.sort(key=lambda x: x[1], reverse=True)
        return [s[0] for s in scores[:top_n]]

    def get_candidates(self, input_products):
        rule_cands = self._get_rule_candidates(input_products)
        semantic_cands = self._get_semantic_candidates(input_products)
        
        # Combine and remove duplicates
        seen = {p["id"] for p in input_products}
        combined = []
        for p in rule_cands + semantic_cands:
            if p["id"] not in seen:
                combined.append(p)
                seen.add(p["id"])
        
        return combined[:15]
