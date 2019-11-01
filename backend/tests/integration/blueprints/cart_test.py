import pytest
from flask import Flask
import json

from blueprints.cart import cart_blueprint
from lib.errors import BaseCartException, error_handler


@pytest.fixture(scope="module")
def test_app():
    test_app = Flask(__name__)

    test_app.register_blueprint(cart_blueprint)

    test_app.register_error_handler(BaseCartException, error_handler)

    yield test_app


@pytest.fixture(scope="module")
def test_client(test_app):
    yield test_app.test_client()


@pytest.fixture()
def test_cart_id(test_client):
    response = test_client.post('/cart')

    cart = response.json

    yield cart.get('cartId')


def test_healthcheck(test_client):
    response = test_client.get("/health")

    assert response.content_type == 'application/json'

    assert response.json == {
        "healthy": True
    }

    assert response.status_code == 200


def test_create_cart_endpoint(test_client):
    response = test_client.post("/cart")

    assert response.content_type == 'application/json'

    cart = response.json

    assert type(cart.get('cartId')) is int
    assert cart.get('cartItems') == {}
    assert response.status_code == 201


def test_get_cart_endpoint(test_client, test_cart_id):
    response = test_client.get('/cart/{}'.format(test_cart_id))

    assert response.content_type == 'application/json'

    cart = response.json

    assert cart.get('cartId') == test_cart_id
    assert cart.get('cartItems') == {}
    assert response.status_code == 200


def test_get_cart_endpoint_cart_doesnt_exist(test_client):
    response = test_client.get('/cart/{}'.format(1))

    assert response.content_type == 'application/json'
    assert response.status_code == 404

    assert response.json == {
        "error": "Cart 1 not found"
    }


def test_clear_cart_endpoint(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 1})

    assert response.status_code == 200

    response = test_client.post('/cart/{}/clear'.format(test_cart_id))

    assert response.status_code == 204
    assert len(response.data) == 0

    response = test_client.get('/cart/{}'.format(test_cart_id))

    assert response.status_code == 200
    assert response.json.get('cartItems') == {}


def test_clear_cart_endpoint_cart_doesnt_exist(test_client):
    response = test_client.post('/cart/{}/clear'.format(1))

    assert response.content_type == 'application/json'
    assert response.status_code == 404

    assert response.json == {
        "error": "Cart 1 not found"
    }


def test_add_item_to_cart_endpoint(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 1})

    assert response.content_type == 'application/json'

    cart = response.json

    assert len(cart.get('cartItems')) == 1
    assert cart.get('cartItems').get("1") == {
        "itemId": 1,
        "quantity": 1
    }


def test_add_item_to_cart_endpoint_no_quantity_provided(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={})

    assert response.content_type == 'application/json'
    assert response.status_code == 400

    assert response.json == {
        "error": "Invalid quantity"
    }


def test_add_item_to_cart_endpoint_invalid_quantity_provided(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": -1})

    assert response.content_type == 'application/json'

    assert response.json == {
        "error": "Invalid quantity"
    }
    assert response.status_code == 400


def test_increment_item_quantity_endpoint(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 1})

    assert response.status_code == 200

    response = test_client.post('/cart/{}/item/{}/increment'.format(test_cart_id, 1))

    assert response.content_type == 'application/json'

    cart = response.json

    assert cart.get('cartItems').get("1").get("quantity") == 2


def test_decrement_item_quantity_endpoint(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 2})

    assert response.status_code == 200

    response = test_client.post('/cart/{}/item/{}/decrement'.format(test_cart_id, 1))

    assert response.content_type == 'application/json'

    cart = response.json

    assert cart.get('cartItems').get("1").get("quantity") == 1


def test_decrement_item_quantity_endpoint_to_zero_clears_cart(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 1})

    assert response.status_code == 200

    response = test_client.post('/cart/{}/item/{}/decrement'.format(test_cart_id, 1))

    assert response.content_type == 'application/json'

    cart = response.json

    assert cart.get('cartItems') == {}


def test_delete_item_from_cart_endpoint(test_client, test_cart_id):
    response = test_client.post('/cart/{}/item/{}'.format(test_cart_id, 1), json={"quantity": 1})

    assert response.status_code == 200

    response = test_client.delete('/cart/{}/item/{}'.format(test_cart_id, 1))

    assert response.status_code == 204
    assert len(response.data) == 0

    response = test_client.get('/cart/{}'.format(test_cart_id))

    assert response.status_code == 200
    assert response.json.get('cartItems') == {}


def test_delete_item_from_cart_endpoint_item_doesnt_exist(test_client, test_cart_id):
    response = test_client.delete('/cart/{}/item/{}'.format(test_cart_id, 1))

    assert response.content_type == 'application/json'
    assert response.status_code == 404

    assert response.json == {
        "error": "Item 1 not found in cart"
    }


def test_bulk_add_items_to_cart_correctly_does_its_thing(test_client, test_cart_id):

    items_to_add = [
        {'item_id': 1, 'quantity': 4},
        {'item_id': 3, 'quantity': 2}
    ]

    response = test_client.post('/cart/{}/items'.format(test_cart_id),
                                data=json.dumps(items_to_add),
                                content_type='application/json')

    assert response.content_type == 'application/json'
    assert response.status_code == 200

    cart = response.json

    assert len(cart.get('cartItems')) == 2
    assert cart.get('cartItems') == {
        "1": {
            "itemId": 1,
            "quantity": 4
        },
        "3": {
            "itemId": 3,
            "quantity": 2
        },
    }


def test_bulk_validates_items_being_added_and_returns_error_with_index(test_client, test_cart_id):

    items_to_add = [
        {'item_id': 1, 'quantity': 4},
        {'item_id': 3},
        {'quantity': 4},
    ]

    response = test_client.post('/cart/{}/items'.format(test_cart_id),
                                data=json.dumps(items_to_add),
                                content_type='application/json')

    assert response.content_type == 'application/json'
    assert response.status_code == 400

    assert response.json == [
        {'index': 1, 'error': 'Invalid quantity'},
        {'index': 2, 'error': 'Missing item ID'}
    ]
