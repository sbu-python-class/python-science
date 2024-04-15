import pytest

@pytest.fixture
def numbers():
    return []

@pytest.fixture
def append_1(numbers):
    numbers.append(1)

@pytest.fixture
def append_2(numbers, append_1):
    numbers.append(2)

def test_initial(numbers):
    assert numbers == []

def test_append_1(numbers, append_1):
    assert numbers == [1]

def test_append_2(numbers, append_2):
    assert numbers == [1, 2]
