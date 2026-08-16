import pytest

from workspace.calculator import *

def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(1, 1) == 1
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ValueError):
        divide(1, 0)
    with pytest.raises(ValueError):
        divide(-1, 0)
    with pytest.raises(ValueError):
        divide(0, 0)