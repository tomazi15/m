from mock import patch, mock
import pytest

from lib.models.cart import Cart
from lib.errors import CartNotFoundException
import lib.storage as storage


def test_get_cart_id_exists():
    with patch.dict(storage._carts, {1: mock.sentinel}):
        assert storage.get_cart(1) == mock.sentinel


def test_get_cart_id_doesnt_exist():
    with patch.dict(storage._carts, {}):
        with pytest.raises(CartNotFoundException):
            storage.get_cart(1)


def test_create_cart():
    with patch.dict(storage._carts, {}):
        cart = storage.create_cart()

        assert isinstance(cart, Cart)
        assert type(cart.id) is int
        assert cart.items == {}
