from flask import Blueprint, jsonify, request

import lib.storage as storage
from lib.models.item import Item
from lib.errors import InvalidQuantityException, MissingItemIdException

cart_blueprint = Blueprint('cart', __name__)


@cart_blueprint.route('/health')
def healthcheck():
    return jsonify({"healthy": True})


@cart_blueprint.route('/cart', methods=['POST'])
def create_cart_endpoint():
    cart = storage.create_cart()

    return jsonify(cart.to_json()), 201


@cart_blueprint.route('/cart/<int:cart_id>', methods=['GET'])
def get_cart_endpoint(cart_id):
    cart = storage.get_cart(cart_id)

    return jsonify(cart.to_json()), 200


@cart_blueprint.route('/cart/<int:cart_id>/clear', methods=['POST'])
def clear_cart_endpoint(cart_id):
    cart = storage.get_cart(cart_id)

    cart.clear()

    return "", 204


@cart_blueprint.route('/cart/<int:cart_id>/items', methods=['POST'])
def bulk_add_item_to_cart_endpoint(cart_id):
    # get_json will refuse to parse the body if there's no 'application/json' Content-Type header set.
    # you could do json.loads(request.data) here instead, but we chose to use get_json's force flag.
    items = request.get_json(force=True)

    validation_errors = []
    for index, item in enumerate(items):
        try:
            if 'quantity' not in item:
                raise InvalidQuantityException
            if 'item_id' not in item:
                raise MissingItemIdException
        except (MissingItemIdException, InvalidQuantityException) as e:
            validation_errors.append({'index': index, 'error': e.message})

    if validation_errors:
        return jsonify(validation_errors), 400

    cart = storage.get_cart(cart_id)
    for item in items:
        item = Item(item['item_id'], item['quantity'])
        cart.add_item(item)
    return jsonify(cart.to_json()), 200


@cart_blueprint.route('/cart/<int:cart_id>/item/<int:item_id>', methods=['POST'])
def add_item_to_cart_endpoint(cart_id, item_id):
    cart = storage.get_cart(cart_id)

    # get_json will refuse to parse the body if there's no 'application/json' Content-Type header set.
    # you could do json.loads(request.data) here instead, but we chose to use get_json's force flag.
    request_body = request.get_json(force=True)

    if 'quantity' not in request_body:
        raise InvalidQuantityException

    quantity = request_body.get('quantity')

    item = Item(item_id, quantity)

    cart.add_item(item)

    return jsonify(cart.to_json()), 200


@cart_blueprint.route('/cart/<int:cart_id>/item/<int:item_id>/increment', methods=['POST'])
def increment_item_quantity_endpoint(cart_id, item_id):
    cart = storage.get_cart(cart_id)

    item = cart.get_item_by_id(item_id)

    item.set_quantity(item.get_quantity() + 1)

    return jsonify(cart.to_json()), 200


@cart_blueprint.route('/cart/<int:cart_id>/item/<int:item_id>/decrement', methods=['POST'])
def decrement_item_quantity_endpoint(cart_id, item_id):
    cart = storage.get_cart(cart_id)

    item = cart.get_item_by_id(item_id)

    quantity = item.get_quantity() - 1

    if quantity == 0:
        cart.remove_item(item)
    else:
        item.set_quantity(quantity)

    return jsonify(cart.to_json()), 200


@cart_blueprint.route('/cart/<int:cart_id>/item/<int:item_id>', methods=['DELETE'])
def delete_item_from_cart_endpoint(cart_id, item_id):
    cart = storage.get_cart(cart_id)

    item = cart.get_item_by_id(item_id)

    cart.remove_item(item)

    return "", 204
