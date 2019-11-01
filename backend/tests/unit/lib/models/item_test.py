import pytest

from lib.models.item import Item
from lib.errors import InvalidQuantityException


@pytest.fixture
def mock_item():
    yield Item(item_id=1, quantity=1)


def test_create_item_with_negative_quantity():
    with pytest.raises(InvalidQuantityException):
        Item(item_id=1, quantity=-1)


def test_create_item_with_quantity_none():
    with pytest.raises(InvalidQuantityException):
        Item(item_id=1, quantity=None)


def test_get_id(mock_item):
    assert mock_item.get_id() == 1


def test_get_quantity(mock_item):
    assert mock_item.get_quantity() == 1


def test_set_quantity_valid_quantity(mock_item):
    mock_item.set_quantity(2)

    assert mock_item.quantity == 2


def test_set_quantity_invalid_quantity_none(mock_item):
    with pytest.raises(InvalidQuantityException):
        mock_item.set_quantity(None)


def test_set_quantity_invalid_quantity_negative(mock_item):
    with pytest.raises(InvalidQuantityException):
        mock_item.set_quantity(-1)


def test_to_json(mock_item):
    assert mock_item.to_json() == {
        "itemId": 1,
        "quantity": 1
    }
