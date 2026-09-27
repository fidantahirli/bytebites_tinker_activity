# ByteBites Models
#
# Classes:
# - Customer: represents a user, tracks name and purchase history
# - MenuItem: represents a single food/drink item with name, price, category, popularity
# - Menu: the full collection of MenuItems, supports filtering by category
# - Transaction: groups selected items into an order and computes total cost

from dataclasses import dataclass, field


@dataclass
class MenuItem:
    name: str
    price: float
    category: str
    popularity_rating: float


@dataclass
class Transaction:
    items: list[MenuItem] = field(default_factory=list)

    def compute_total(self) -> float:
        pass


@dataclass
class Menu:
    items: list[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem) -> None:
        pass

    def filter_by_category(self, category: str) -> list[MenuItem]:
        pass


@dataclass
class Customer:
    name: str
    purchase_history: list[Transaction] = field(default_factory=list)

    def is_verified(self) -> bool:
        pass
