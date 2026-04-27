
class LLMLayer:
    def generate_reasoning(self, input_products, bundle_items, conversion_prob):
        input_names = ", ".join([p["name"] for p in input_products])
        bundle_names = " and ".join([p["name"] for p in bundle_items])
        
        cats = {p["category"] for p in bundle_items} | {p["category"] for p in input_products}
        
        context = "daily care completeness"
        if "feeding" in cats: context = "efficient feeding and cleaning"
        if "toys" in cats: context = "interactive playtime and sensory development"
        if "baby_care" in cats: context = "comprehensive hygiene and skin protection"

        # Likelihood rationale
        likelihood_msg = "This bundle covers essential daily needs, making it highly likely to be added together in a single purchase."
        if conversion_prob > 0.8:
            likelihood_msg = "This high-utility combination matches common purchasing patterns, ensuring a seamless care routine."
        elif conversion_prob < 0.6:
            likelihood_msg = "While slightly different categories, these items offer unique value to your baby's growth and hygiene."

        en_reasoning = f"These items are commonly used together for {context} ({input_names} + {bundle_names}). {likelihood_msg}"
        
        ar_context = "العناية اليومية المتكاملة"
        if "feeding" in cats: ar_context = "التغذية والنظافة الفعالة"
        if "toys" in cats: ar_context = "وقت اللعب التفاعلي وتنمية الحواس"
        if "baby_care" in cats: ar_context = "النظافة الشاملة وحماية بشرة الطفل"

        ar_reasoning = f"تُستخدم هذه المنتجات معاً بشكل أساسي من أجل {ar_context}. هذا المزيج يغطي الاحتياجات اليومية الأساسية، مما يجعله خياراً مثالياً للاقتناء في سلة واحدة لضمان روتين متكامل."
        
        return en_reasoning, ar_reasoning, 0.9

def estimate_aov_lift_legacy(bundle_items):
    return 35 if len(bundle_items) >= 2 else 15
