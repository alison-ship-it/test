"""Service layer that ties models and utilities together."""

from src.models import User, Product, Order
from src.utils import is_valid_email


class UserService:
    """Manages user operations backed by an in-memory store."""

    def __init__(self):
        self._users = {}
        self._next_id = 1

    def create_user(self, name, email):
        if not is_valid_email(email):
            raise ValueError(f"Invalid email: {email}")
        user = User(self._next_id, name, email)
        self._users[user.user_id] = user
        self._next_id += 1
        return user

    def get_user(self, user_id):
        return self._users.get(user_id)

    def list_users(self):
        return list(self._users.values())


class OrderService:
    """Manages order operations."""

    def __init__(self):
        self._orders = {}
        self._next_id = 1

    def create_order(self, user):
        order = Order(self._next_id, user)
        self._orders[order.order_id] = order
        self._next_id += 1
        return order

    def get_order(self, order_id):
        return self._orders.get(order_id)

    def orders_for_user(self, user_id):
        return [o for o in self._orders.values() if o.user.user_id == user_id]
