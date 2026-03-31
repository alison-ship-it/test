"""Domain models for the application."""


class User:
    """Represents a user in the system."""

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name!r})"

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email}


class Product:
    """Represents a product in the catalog."""

    def __init__(self, product_id, name, price, category="general"):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name!r}, price={self.price})"

    def apply_discount(self, percentage):
        """Return a new price after applying a discount percentage."""
        if not 0 <= percentage <= 100:
            raise ValueError("Discount must be between 0 and 100")
        return round(self.price * (1 - percentage / 100), 2)


class Order:
    """Represents a customer order."""

    def __init__(self, order_id, user, items=None):
        self.order_id = order_id
        self.user = user
        self.items = items or []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    @property
    def total(self):
        return sum(
            item["product"].price * item["quantity"] for item in self.items
        )
