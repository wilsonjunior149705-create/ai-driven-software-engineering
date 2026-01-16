from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class LineItem:
    sku: str
    unit_price: float
    quantity: int


@dataclass(frozen=True)
class Quote:
    subtotal: float
    discount: float
    shipping: float
    total: float


# Gerado com o prompt (Copilot):
# "Crie uma função em Python que calcule o total de um pedido com:
#  - itens (sku, preço unitário, quantidade)
#  - cupom opcional (PERCENT10, PERCENT20, FIXED15)
#  - regras: subtotal = soma(preço*quantidade)
#            desconto: percentuais limitados a 50 no máximo; FIXED não pode passar do subtotal
#            frete: grátis se subtotal >= 200 após desconto; caso contrário 20
#  - validações: preço >= 0, quantidade >= 1
#  - retorne subtotal, desconto, frete e total"
def calculate_quote(items: Iterable[LineItem], coupon: Optional[str] = None) -> Quote:
    items_list = list(items)
    if not items_list:
        raise ValueError("Order must contain at least one item.")

    subtotal = 0.0
    for it in items_list:
        if it.unit_price < 0:
            raise ValueError("unit_price must be >= 0")
        if it.quantity < 1:
            raise ValueError("quantity must be >= 1")
        subtotal += it.unit_price * it.quantity

    coupon = (coupon or "").strip().upper()
    discount = 0.0

    if coupon == "PERCENT10":
        discount = 0.10 * subtotal
    elif coupon == "PERCENT20":
        discount = 0.20 * subtotal
    elif coupon == "FIXED15":
        discount = 15.0
    elif coupon in ("", "NONE"):
        discount = 0.0
    else:
        raise ValueError("Invalid coupon")

    # Proteções básicas
    discount = min(discount, 0.50 * subtotal)   # teto 50%
    discount = min(discount, subtotal)          # nunca passa do subtotal
    discount = max(discount, 0.0)

    after_discount = subtotal - discount
    shipping = 0.0 if after_discount >= 200.0 else 20.0
    total = after_discount + shipping

    # Arredondamento amigável para dinheiro
    def money(x: float) -> float:
        return round(x + 1e-9, 2)

    return Quote(
        subtotal=money(subtotal),
        discount=money(discount),
        shipping=money(shipping),
        total=money(total),
    )
