import pytest
from shopping_cart import ShoppingCart
from unittest.mock import patch


@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1, 3)
    cart.add_item("banana", 0.5, 5)
    return cart

def test_add_item_changes_quantity_expected_way(empty_cart):
    empty_cart.add_item("apple", 1, 2)
    assert empty_cart.items["apple"]["quantity"] == 2

def test_add_item_does_not_affect_price(empty_cart):
    empty_cart.add_item("apple", 1, 2)
    empty_cart.add_item("apple", 1, 2)
    assert empty_cart.items["apple"]["unit_price"] == 1

@pytest.mark.parametrize("item_name, unit_price, quantity, expected_exception",
                         [
                             ("orange", -1, 1, ValueError),
                             ("orange", 1, 0, ValueError),
                             ("orange", 1, -2, ValueError),
                         ])
def test_add_item_invalid_input(empty_cart, item_name, unit_price, quantity, expected_exception):
    with pytest.raises(expected_exception):
        empty_cart.add_item(item_name, unit_price, quantity)


@patch('shopping_cart.ShoppingCart.get_discount_multiplier', return_value=0.1)
def test_checkout(mock_get_discount_multiplier, cart_with_items):
    final_price = cart_with_items.checkout("SAVE10")
    assert final_price == 4.95

    
