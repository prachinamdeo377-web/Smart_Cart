# ============================================================
#  ml_engine.py — AI/ML Brain
#  Budget status, predictions, suggestions — sab yahan
# ============================================================

from collections import defaultdict


def get_budget_status(total_spent, budget):
    """Budget ka % calculate karo — green/yellow/red decide karta hai"""
    if budget <= 0:
        return {"status":"no_budget","color":"gray","percent":0,"message":"Pehle budget set karo"}

    percent = (total_spent / budget) * 100

    if percent <= 50:
        return {"status":"safe","color":"green","percent":round(percent,1),
                "message":f"Budget ka sirf {percent:.0f}% use hua — bilkul safe! ✅"}
    elif percent <= 75:
        return {"status":"moderate","color":"yellow","percent":round(percent,1),
                "message":f"Budget ka {percent:.0f}% use ho gaya — dhyan rakho 🟡"}
    elif percent <= 90:
        return {"status":"warning","color":"orange","percent":round(percent,1),
                "message":f"⚠️ Budget ka {percent:.0f}% use ho gaya — ruko!"}
    elif percent <= 100:
        return {"status":"critical","color":"red","percent":round(percent,1),
                "message":f"🚨 Budget sirf {100-percent:.0f}% bacha hai!"}
    else:
        return {"status":"exceeded","color":"darkred","percent":round(percent,1),
                "message":f"❌ Budget {percent-100:.0f}% exceed! Kuch items hataao."}


def get_category_breakdown(cart_items):
    """Category-wise kitna kharch hua"""
    breakdown = defaultdict(float)
    for item in cart_items:
        breakdown[item.get("category","Other")] += \
            item.get("discounted_price", item.get("actual_price",0)) * item.get("quantity",1)
    return dict(sorted(breakdown.items(), key=lambda x: x[1], reverse=True))


def predict_final_bill(cart_items):
    """
    ML Prediction: abhi tak ke average se estimate karo
    ki 25 items pe final bill kitna hoga
    """
    if not cart_items:
        return 0
    total_qty   = sum(i.get("quantity",1) for i in cart_items)
    total_spent = sum(i.get("discounted_price",0) * i.get("quantity",1) for i in cart_items)
    if total_qty == 0:
        return 0
    return round((total_spent / total_qty) * 25, 2)


def get_smart_suggestions(cart_items, budget):
    """Agar budget exceed ho toh top 3 expensive items hatane ka suggest karo"""
    if budget <= 0:
        return []
    total = sum(i.get("discounted_price",0) * i.get("quantity",1) for i in cart_items)
    if total <= budget:
        return []
    sorted_items = sorted(cart_items,
        key=lambda x: x.get("discounted_price",0) * x.get("quantity",1), reverse=True)
    return [
        {"product_id": i["id"], "product_name": i["name"],
         "saving": i.get("discounted_price",0)*i.get("quantity",1),
         "message": f"'{i['name']}' hataane se ₹{i.get('discounted_price',0)*i.get('quantity',1):.0f} bachega"}
        for i in sorted_items[:3]
    ]


def get_savings_summary(cart_items):
    """Discounts se kitni savings mili"""
    actual     = sum(i.get("actual_price",0)      * i.get("quantity",1) for i in cart_items)
    discounted = sum(i.get("discounted_price",actual) * i.get("quantity",1) for i in cart_items)
    savings    = actual - discounted
    return {
        "total_actual":      round(actual, 2),
        "total_discounted":  round(discounted, 2),
        "total_savings":     round(savings, 2),
        "savings_percent":   round(savings/actual*100, 1) if actual > 0 else 0
    }