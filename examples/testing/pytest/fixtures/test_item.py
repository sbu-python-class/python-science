import pytest
from shopping_cart import Item

@pytest.fixture
def a():
    return Item("apple", 10)

@pytest.fixture
def b():
    return Item("banana", 20)

@pytest.fixture
def c():
    return Item("apple", 20)

def test_add(a, c):
    # note: each test gets its own copy of the fixture results, so any
    # modifications don't impact other tests
    a += c
    assert a.quantity == 30

def test_repr(a, b, c):
    assert repr(a) == "apple: 10"
    assert repr(b) == "banana: 20"
    assert repr(c) == "apple: 20"

def test_invalid_add(a, b):
    with pytest.raises(ValueError, match="names don't match"):
        a + b

def test_invalid_name():
    with pytest.raises(ValueError, match="invalid item name"):
        d = Item("dog")

def test_equality(a, b, c):
    assert a != b
    assert a == c


@pytest.fixture
def items(a, b):
    items = []
    items.append(a)
    items.append(b)
    return items

def test_item_list(items, c):
    assert c in items
