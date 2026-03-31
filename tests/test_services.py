"""Tests for src.services."""

import pytest
from src.services import UserService, OrderService
from src.models import Product


class TestUserService:
    def test_create_and_get(self):
        svc = UserService()
        user = svc.create_user("Alice", "alice@example.com")
        assert svc.get_user(user.user_id) is user

    def test_invalid_email(self):
        svc = UserService()
        with pytest.raises(ValueError):
            svc.create_user("Bob", "not-an-email")

    def test_list_users(self):
        svc = UserService()
        svc.create_user("Alice", "alice@example.com")
        svc.create_user("Bob", "bob@example.com")
        assert len(svc.list_users()) == 2


class TestOrderService:
    def test_create_order_and_total(self):
        user_svc = UserService()
        user = user_svc.create_user("Alice", "alice@example.com")
        order_svc = OrderService()
        order = order_svc.create_order(user)
        order.add_item(Product(1, "Widget", 10.0), quantity=3)
        assert order.total == 30.0

    def test_orders_for_user(self):
        user_svc = UserService()
        user = user_svc.create_user("Alice", "alice@example.com")
        order_svc = OrderService()
        order_svc.create_order(user)
        order_svc.create_order(user)
        assert len(order_svc.orders_for_user(user.user_id)) == 2
