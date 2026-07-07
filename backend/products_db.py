# ============================================================
#  products_db.py — Mall ke saare products yahan hain
#  Naya product add karna ho toh same format mein
#  neeche add karo
# ============================================================

PRODUCTS = {
    "P001": {"id":"P001","name":"Amul Butter 500g","category":"Dairy","actual_price":280,"discounted_price":252,"discount_percent":10,"unit":"500g","emoji":"🧈"},
    "P002": {"id":"P002","name":"Britannia Bread","category":"Bakery","actual_price":55,"discounted_price":55,"discount_percent":0,"unit":"400g","emoji":"🍞"},
    "P003": {"id":"P003","name":"India Gate Basmati Rice","category":"Grains","actual_price":420,"discounted_price":378,"discount_percent":10,"unit":"5kg","emoji":"🍚"},
    "P004": {"id":"P004","name":"Tata Salt","category":"Grocery","actual_price":28,"discounted_price":25,"discount_percent":11,"unit":"1kg","emoji":"🧂"},
    "P005": {"id":"P005","name":"Surf Excel Detergent","category":"Household","actual_price":220,"discounted_price":198,"discount_percent":10,"unit":"1kg","emoji":"🧺"},
    "P006": {"id":"P006","name":"Lay's Classic Chips","category":"Snacks","actual_price":40,"discounted_price":40,"discount_percent":0,"unit":"73g","emoji":"🍟"},
    "P007": {"id":"P007","name":"Maggi Noodles (Pack of 12)","category":"Instant Food","actual_price":156,"discounted_price":140,"discount_percent":10,"unit":"12 pack","emoji":"🍜"},
    "P008": {"id":"P008","name":"Colgate Toothpaste","category":"Personal Care","actual_price":110,"discounted_price":99,"discount_percent":10,"unit":"200g","emoji":"🪥"},
    "P009": {"id":"P009","name":"Aashirvaad Atta","category":"Grains","actual_price":350,"discounted_price":315,"discount_percent":10,"unit":"5kg","emoji":"🌾"},
    "P010": {"id":"P010","name":"Vim Dishwash Liquid","category":"Household","actual_price":99,"discounted_price":89,"discount_percent":10,"unit":"500ml","emoji":"🍶"},
    "P011": {"id":"P011","name":"Mother Dairy Milk","category":"Dairy","actual_price":62,"discounted_price":62,"discount_percent":0,"unit":"1L","emoji":"🥛"},
    "P012": {"id":"P012","name":"Haldiram's Bhujia","category":"Snacks","actual_price":140,"discounted_price":126,"discount_percent":10,"unit":"400g","emoji":"🥜"},
    "P013": {"id":"P013","name":"Dettol Handwash","category":"Personal Care","actual_price":85,"discounted_price":76,"discount_percent":11,"unit":"200ml","emoji":"🧴"},
    "P014": {"id":"P014","name":"Tropicana Orange Juice","category":"Beverages","actual_price":120,"discounted_price":108,"discount_percent":10,"unit":"1L","emoji":"🍊"},
    "P015": {"id":"P015","name":"Bournvita","category":"Beverages","actual_price":280,"discounted_price":252,"discount_percent":10,"unit":"500g","emoji":"☕"},
    "P016": {"id":"P016","name":"Fortune Sunflower Oil","category":"Grocery","actual_price":185,"discounted_price":166,"discount_percent":10,"unit":"1L","emoji":"🫙"},
    "P017": {"id":"P017","name":"Parle-G Biscuits","category":"Snacks","actual_price":10,"discounted_price":10,"discount_percent":0,"unit":"100g","emoji":"🍪"},
    "P018": {"id":"P018","name":"Tata Tea Premium","category":"Beverages","actual_price":195,"discounted_price":175,"discount_percent":10,"unit":"500g","emoji":"🍵"},
    "P019": {"id":"P019","name":"Lifebuoy Soap (Pack of 4)","category":"Personal Care","actual_price":80,"discounted_price":72,"discount_percent":10,"unit":"4 bars","emoji":"🧼"},
    "P020": {"id":"P020","name":"Onion (Loose)","category":"Vegetables","actual_price":60,"discounted_price":60,"discount_percent":0,"unit":"1kg","emoji":"🧅"},
}

def get_all_products():
    return list(PRODUCTS.values())

def get_product(product_id):
    return PRODUCTS.get(product_id)