import pytest
import shopping_cart


@pytest.fixture
def a():
    return shopping_cart.Item("apple", 10)

@pytest.fixture
def b():
    return shopping_cart.Item("banana", 20)

@pytest.fixture
def c():
    return shopping_cart.Item("apple", 20)

def test_add(a, c):
    # modifies a
    a += c
    assert a.quantity == 30

def test_repr(a, b, c):
    # receives unmodified a
    assert repr(a) == "apple: 10"
    assert repr(b) == "banana: 20"
    assert repr(c) == "apple: 20"

def test_equality(a, b, c):
    assert a != b
    assert a == c

def test_invalid_add(a, b):
    with pytest.raises(ValueError, match="names don't match"):
        a + b

def test_invalid_name():
    with pytest.raises(ValueError, match="invalid item name"):
        d = shopping_cart.Item("dog")
