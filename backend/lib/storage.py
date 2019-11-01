from random import randint
from lib.models.cart import Cart
from lib.errors import CartNotFoundException


_carts = {}


def get_cart(cart_id):
    if cart_id not in _carts:
        raise CartNotFoundException(cart_id)

    return _carts.get(cart_id)


def create_cart():
    cart_id = randint(0, 1024)
    _carts[cart_id] = Cart(cart_id)
    return _carts.get(cart_id)
