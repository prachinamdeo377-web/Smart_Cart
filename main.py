# ============================================================
#  main.py — FastAPI Backend Server
#  Yeh poora backend hai — frontend isse baat karta hai
#  Chalane ke liye: python main.py
# ============================================================

import sys, os, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.products_db import get_product, get_all_products
from ml.ml_engine import (
    get_budget_status, get_category_breakdown,
    predict_final_bill, get_smart_suggestions, get_savings_summary
)

# ── App Setup ───────────────────────────────────────────────
app = FastAPI(title="Smart Cart API")

app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ── Frontend files serve karo ───────────────────────────────
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=FileResponse)
def serve_frontend():
    return FileResponse("frontend/index.html")

# ── Cart data RAM mein ──────────────────────────────────────
carts = {}  # { session_id: { "items": {}, "budget": 0 } }


# ── Request Models ──────────────────────────────────────────
class BudgetReq(BaseModel):
    session_id: str
    budget: float

class ItemReq(BaseModel):
    session_id: str
    product_id: str


# ── Helper ──────────────────────────────────────────────────
def get_or_create(sid):
    if sid not in carts:
        carts[sid] = {"items": {}, "budget": 0}
    return carts[sid]

def cart_response(sid):
    cart   = get_or_create(sid)
    items  = list(cart["items"].values())
    budget = cart["budget"]
    total_disc   = sum(i["discounted_price"] * i["quantity"] for i in items)
    total_actual = sum(i["actual_price"]     * i["quantity"] for i in items)
    return {
        "session_id":           sid,
        "items":                items,
        "total_items":          sum(i["quantity"] for i in items),
        "total_actual":         round(total_actual, 2),
        "total_discounted":     round(total_disc,   2),
        "budget":               budget,
        "budget_status":        get_budget_status(total_disc, budget),
        "category_breakdown":   get_category_breakdown(items),
        "savings_summary":      get_savings_summary(items),
        "smart_suggestions":    get_smart_suggestions(items, budget),
        "predicted_final_bill": predict_final_bill(items),
    }


# ══════════════════════════════════════════════════════════
#  API ROUTES
# ══════════════════════════════════════════════════════════

@app.get("/api/products")
def products():
    return {"products": get_all_products()}

@app.post("/api/cart/new")
def new_cart():
    sid = str(uuid.uuid4())[:8].upper()
    carts[sid] = {"items": {}, "budget": 0}
    return {"session_id": sid}

@app.post("/api/cart/budget")
def set_budget(r: BudgetReq):
    get_or_create(r.session_id)["budget"] = r.budget
    return cart_response(r.session_id)

@app.post("/api/cart/add")
def add_item(r: ItemReq):
    cart    = get_or_create(r.session_id)
    product = get_product(r.product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    pid = r.product_id
    if pid in cart["items"]:
        cart["items"][pid]["quantity"] += 1
    else:
        cart["items"][pid] = {**product, "quantity": 1}
    return cart_response(r.session_id)

@app.post("/api/cart/remove")
def remove_item(r: ItemReq):
    cart = get_or_create(r.session_id)
    pid  = r.product_id
    if pid not in cart["items"]:
        raise HTTPException(404, "Item not found in the cart")
    if cart["items"][pid]["quantity"] > 1:
        cart["items"][pid]["quantity"] -= 1
    else:
        del cart["items"][pid]
    return cart_response(r.session_id)

@app.get("/api/cart/{sid}")
def get_cart(sid: str):
    return cart_response(sid)

@app.delete("/api/cart/{sid}/clear")
def clear_cart(sid: str):
    get_or_create(sid)["items"] = {}
    return cart_response(sid)


# ── Server Chalao ───────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*45)
    print("  🛒  SMART CART is starting!")
    print("="*45)
    print("  Browser mein kholao:")
    print("  👉  http://localhost:8000")
    print("="*45 + "\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)