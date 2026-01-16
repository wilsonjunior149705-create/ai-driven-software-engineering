import pytest
from app.pricing import LineItem, calculate_quote


# Gerado com o prompt (Copilot):
# "Crie testes pytest para a função calculate_quote cobrindo:
#  - sem cupom
#  - cupom percentual
#  - cupom fixo
#  - frete grátis vs frete pago
#  - validações (preço negativo, quantidade inválida, lista vazia, cupom inválido)"
def test_no_coupon_shipping_paid():
    items = [LineItem("A", 50.0, 2)]  # subtotal 100
    q = calculate_quote(items, None)
    assert q.subtotal == 100.00
    assert q.discount == 0.00
    assert q.shipping == 20.00
    assert q.total == 120.00


def test_percent_coupon_and_shipping_paid():
    items = [LineItem("A", 50.0, 2)]  # subtotal 100
    q = calculate_quote(items, "PERCENT10")  # desconto 10
    assert q.subtotal == 100.00
    assert q.discount == 10.00
    assert q.shipping == 20.00
    assert q.total == 110.00


def test_fixed_coupon_shipping_free():
    items = [LineItem("A", 120.0, 2)]  # subtotal 240
    q = calculate_quote(items, "FIXED15")  # after_discount 225 => frete 0
    assert q.subtotal == 240.00
    assert q.discount == 15.00
    assert q.shipping == 0.00
    assert q.total == 225.00


def test_discount_never_exceeds_subtotal_and_respects_50_percent_cap():
    items = [LineItem("A", 10.0, 1)]  # subtotal 10
    q = calculate_quote(items, "FIXED15")  # desconto 15 → limitado a 50%
    assert q.subtotal == 10.00
    assert q.discount == 5.00
    assert q.shipping == 20.00
    assert q.total == 25.00



def test_invalid_coupon_raises():
    items = [LineItem("A", 10.0, 1)]
    with pytest.raises(ValueError):
        calculate_quote(items, "INVALID")


def test_empty_items_raises():
    with pytest.raises(ValueError):
        calculate_quote([], None)


def test_negative_price_raises():
    items = [LineItem("A", -1.0, 1)]
    with pytest.raises(ValueError):
        calculate_quote(items, None)


def test_invalid_quantity_raises():
    items = [LineItem("A", 10.0, 0)]
    with pytest.raises(ValueError):
        calculate_quote(items, None)
