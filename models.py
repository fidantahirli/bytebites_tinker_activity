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
        return float(sum(item.price for item in self.items))


@dataclass
class Menu:
    items: list[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[MenuItem]:
        return [item for item in self.items if item.category == category]


@dataclass
class Customer:
    name: str
    purchase_history: list[Transaction] = field(default_factory=list)

    def is_verified(self) -> bool:
        return len(self.purchase_history) > 0


if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 8.99, "Food", 4.5)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 4.0)
    lemonade = MenuItem("Lemonade", 2.99, "Drinks", 4.2)
    cake = MenuItem("Chocolate Cake", 4.25, "Desserts", 4.8)

    menu = Menu()
    for item in (burger, soda, lemonade, cake):
        menu.add_item(item)
    print(f"Menu has {len(menu.items)} items")

    drinks = menu.filter_by_category("Drinks")
    print("Drinks:", [item.name for item in drinks])

    transaction = Transaction([burger, soda, cake])
    print(f"Transaction total: ${transaction.compute_total():.2f}")
