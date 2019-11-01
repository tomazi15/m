from lib.errors import InvalidQuantityException


class Item:

    def __init__(self, item_id, quantity=1):
        self.id = item_id

        if quantity is None or quantity < 1:
            raise InvalidQuantityException

        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity is None or quantity < 1:
            raise InvalidQuantityException

        self.quantity = quantity

    def to_json(self):
        return {
            "itemId": self.get_id(),
            "quantity": self.get_quantity()
        }
