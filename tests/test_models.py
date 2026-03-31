"""Tests for src.models."""

import pytest
from src.models import User, Product, Order


class TestUser:
    def test_to_dict(self):
        user = User(1, "Alice", "alice@example.com")
        assert user.to_dict() == {
            "user_id": 1,
            "name": "Alice",
            "email": "alice@example.com",
        }

    def test_repr(self):
        user = User(1, "Alice", "alice@example.com")
        assert "Alice" in repr(user)


class TestProduct:
    def test_apply_discount(self):
        product = Product(1, "Widget", 100.0)
        assert product.apply_discount(25) == 75.0

    def test_discount_bounds(self):
        product = Product(1, "Widget", 100.0)
        with pytest.raises(ValueError):
            product.apply_discount(110)


class TestOrder:
    def test_total(self):
        user = User(1, "Alice", "alice@example.com")
        p1 = Product(1, "Widget", 10.0)
        p2 = Product(2, "Gadget", 25.0)
        order = Order(1, user)
        order.add_item(p1, quantity=2)
        order.add_item(p2, quantity=1)
        assert order.total == 45.0
