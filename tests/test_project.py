import pytest
from workspace.calculator import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(-2, -3) == 1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0
    assert divide(1, 0) == 'Error: Division by zero'
    assert divide(-10, 2) == -5
    assert divide(-5, 2) == -2.5
    assert divide(-10, -2) == 5
    assert divide(-5, -2) == 2.5

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10, 20, 30]) == 20.0
    assert average([0, 0, 0]) == 0.0
    assert average([]) == 0.0
    assert average([-1, -2, -3, -4, -5]) == -3.0