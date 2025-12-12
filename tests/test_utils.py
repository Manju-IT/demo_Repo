from utils import add_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3

def test_add_numbers_negative():
    assert add_numbers(-1, -2) == -3

def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0
    