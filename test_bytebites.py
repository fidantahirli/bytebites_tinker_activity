import pytest

from models import Customer, MenuItem, Menu, Transaction


@pytest.fixture
def burger():
    return MenuItem("Spicy Burger", 8.99, "Food", 4.5)


@pytest.fixture
def soda():
    return MenuItem("Large Soda", 2.49, "Drinks", 4.0)


@pytest.fixture
def lemonade():
    return MenuItem("Lemonade", 2.99, "Drinks", 4.2)


@pytest.fixture
def cake():
    return MenuItem("Chocolate Cake", 4.25, "Desserts", 4.8)


@pytest.fixture
def menu(burger, soda, lemonade, cake):
    return Menu([burger, soda, lemonade, cake])


def test_filter_returns_only_matching_category(menu, soda, lemonade):
    assert menu.filter_by_category("Drinks") == [soda, lemonade]


def test_filter_with_no_matches_returns_empty_list(menu):
    assert menu.filter_by_category("Pizza") == []


def test_filter_is_case_sensitive(menu):
    assert menu.filter_by_category("drinks") == []


def test_total_sums_item_prices(burger, soda, cake):
    transaction = Transaction([burger, soda, cake])
    assert transaction.compute_total() == pytest.approx(15.73)


def test_total_of_empty_transaction_is_zero():
    assert Transaction().compute_total() == pytest.approx(0.0)


def test_total_counts_duplicate_items(soda):
    transaction = Transaction([soda, soda])
    assert transaction.compute_total() == pytest.approx(4.98)


def test_new_customer_is_not_verified():
    assert Customer("Alex").is_verified() is False


def test_customer_with_purchase_is_verified(soda):
    customer = Customer("Alex")
    customer.purchase_history.append(Transaction([soda]))
    assert customer.is_verified() is True
