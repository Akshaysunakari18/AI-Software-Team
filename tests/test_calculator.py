import pytest
from workspace.calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, 200) == 300

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    assert subtract(100, 200) == -100

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, -1) == 1
    assert multiply(0, 0) == 0
    assert multiply(100, 200) == 20000

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, -2) == 5
    assert divide(0, 1) == 0
    assert divide(100, 200) == 0.5
    with pytest.raises(ValueError):
        divide(10, 0)