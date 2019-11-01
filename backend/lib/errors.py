from flask import jsonify


class BaseCartException(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            "error": self.message
        }


class CartNotFoundException(BaseCartException):
    def __init__(self, cart_id):
        message = "Cart {} not found".format(cart_id)
        super().__init__(message=message, status_code=404)


class ItemNotFoundException(BaseCartException):
    def __init__(self, item_id):
        message = "Item {} not found in cart".format(item_id)
        super().__init__(message=message, status_code=404)


class InvalidQuantityException(BaseCartException):
    def __init__(self):
        super().__init__(message="Invalid quantity", status_code=400)


class MissingItemIdException(BaseCartException):
    def __init__(self):
        super().__init__(message="Missing item ID", status_code=400)


def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
