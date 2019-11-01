from lib.errors import ItemNotFoundException


class Cart:

    def __init__(self, cart_id):
        self.id = cart_id
        self.items = {}

    def get_id(self):
        return self.id

    def get_items(self):
        return self.items

    def get_item_by_id(self, item_id):
        if item_id not in self.items:
            raise ItemNotFoundException(item_id)
        else:
            return self.items.get(item_id)

    def add_item(self, item):
        self.items[item.get_id()] = item

    def remove_item(self, item):
        self.items.pop(item.get_id())

    def clear(self):
        self.items.clear()

    def to_json(self):
        return {
            "cartId": self.get_id(),
            "cartItems": {id: item.to_json() for id, item in self.get_items().items()}
        }
