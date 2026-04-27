
class LLMLayer:
    def generate_reasoning(self, input_products, bundle_items, conversion_prob):
        input_names = ", ".join([p["name"] for p in input_products])
        bundle_names = " and ".join([p["name"] for p in bundle_items])
        
        cats = {p["category"] for p in bundle_items} | {p["category"] for p in input_products}
        
        bundle_cats = {p["category"] for p in bundle_items}
        
        # Precision Context: Focus on the bundle's specific contribution
        if len(bundle_cats) == 1:
            cat = list(bundle_cats)[0]
            if cat == "feeding": context = "efficient feeding and cleaning"
            elif cat == "toys": context = "interactive playtime and sensory development"
            elif cat == "baby_care": context = "comprehensive hygiene and skin protection"
            else: context = "daily care completeness"
        else:
            context = "all-around baby care"

        # Likelihood rationale
        likelihood_msg = "This bundle covers essential daily needs, making it highly likely to be added together in a single purchase."
        if conversion_prob > 0.8:
            likelihood_msg = "This high-utility combination matches common purchasing patterns, ensuring a seamless care routine."
        elif conversion_prob < 0.6:
            likelihood_msg = "While slightly different categories, these items offer unique value to your baby's growth and hygiene."

        # Focused reasoning
        en_reasoning = f"Adding {bundle_names} to your collection optimizes your {context} routine. {likelihood_msg}"
        
        ar_context = "العناية اليومية المتكاملة"
        if len(bundle_cats) == 1:
            cat = list(bundle_cats)[0]
            if cat == "feeding": ar_context = "التغذية والنظافة الفعالة"
            elif cat == "toys": ar_context = "وقت اللعب التفاعلي وتنمية الحواس"
            elif cat == "baby_care": ar_context = "النظافة الشاملة وحماية بشرة الطفل"
        else:
            ar_context = "الرعاية الشاملة والأساسية لطفلك"

        ar_reasoning = f"إضافة {bundle_names} إلى سلتك يعزز من روتين {ar_context}. هذا المزيج المدروس يضمن لك الحصول على أفضل قيمة وتغطية احتياجات طفلك اليومية الأساسية."
        
        return en_reasoning, ar_reasoning, 0.95

def estimate_aov_lift_legacy(bundle_items):
    return 35 if len(bundle_items) >= 2 else 15
