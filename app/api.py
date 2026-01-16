from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

from app.pricing import LineItem, calculate_quote


app = FastAPI(title="AI-Driven Quote API", version="1.0.0")


class ItemIn(BaseModel):
    sku: str = Field(..., min_length=1)
    unit_price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)


class QuoteRequest(BaseModel):
    items: List[ItemIn]
    coupon: Optional[str] = None


class QuoteResponse(BaseModel):
    subtotal: float
    discount: float
    shipping: float
    total: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/quote", response_model=QuoteResponse)
def quote(req: QuoteRequest):
    items = [LineItem(sku=i.sku, unit_price=i.unit_price, quantity=i.quantity) for i in req.items]
    q = calculate_quote(items, coupon=req.coupon)
    return QuoteResponse(subtotal=q.subtotal, discount=q.discount, shipping=q.shipping, total=q.total)
