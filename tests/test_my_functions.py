import pytest
import time

from source import my_functions as my_functions

def test_add():
    result = my_functions.add(number_one=1, number_two=2)
    assert result == 3

def test_add_string():
    result = my_functions.add("j'aime les", " tests")
    assert result == "j'aime les tests"

def test_divide():
    result = my_functions.divide(number_one=1, number_two=2)
    assert result == 0.5

def test_divide_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one=1,number_two=0)

def test_multiply_zero():
    result = my_functions.multiply(number_one=0,number_two=3)
    assert result == 0

def test_multiply_positif():
    result = my_functions.multiply(number_one=2, number_two=3)
    assert result == 6

def test_multiply_negatif():
    result = my_functions.multiply(number_one=-2, number_two=3)
    assert result == -6

@pytest.mark.slow
def test_multiply_slow():
    time.sleep(5)
    result = my_functions.multiply(number_one=5, number_two=0)
    assert result == 0

@pytest.mark.skip(reason="broken")
def test_add_one():
    result = my_functions.add(number_one=5, number_two=2)
    assert result == 10

@pytest.mark.xfail(reason="bug wip")
def test_add_two():
    result = my_functions.add(number_one=5, number_two=2)
    assert result == 10