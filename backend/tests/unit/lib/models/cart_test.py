import pytest
import mock

from lib.models.cart import Cart
from lib.errors import ItemNotFoundException


@pytest.fixture
def mock_item():
    mock_item = mock.Mock()
    mock_item.id = 1
    mock_item.quantity = 1
    mock_item.get_id.return_value = 1
    mock_item.to_json.return_value = {
        "itemId": 1,
        "quantity": 1
    }
    yield mock_item


@pytest.fixture
def mock_cart(mock_item):
    cart = Cart(cart_id=1)
    cart.items = {1: mock_item}
    yield cart


def test_get_id(mock_cart):
    assert mock_cart.get_id() == 1


def test_get_items(mock_cart, mock_item):
    assert mock_cart.get_items() == {1: mock_item}


def test_get_item_by_id_item_exists(mock_cart, mock_item):
    assert mock_cart.get_item_by_id(1) == mock_item


def test_get_item_by_id_item_doesnt_exist(mock_cart):
    with pytest.raises(ItemNotFoundException):
        mock_cart.get_item_by_id(2)


def test_add_item(mock_cart, mock_item):
    mock_item_2 = mock.Mock()
    mock_item_2.id = 2
    mock_item_2.get_id.return_value = 2

    mock_cart.add_item(mock_item_2)

    assert mock_cart.items == {1: mock_item, 2: mock_item_2}


def test_remove_item(mock_cart, mock_item):
    mock_cart.remove_item(mock_item)

    assert mock_cart.items == {}


def test_clear(mock_cart):
    mock_cart.clear()

    assert mock_cart.items == {}


def test_to_json(mock_cart, mock_item):
    assert mock_cart.to_json() == {
        "cartId": 1,
        "cartItems": {
            1: mock_item.to_json()
        }
    }
