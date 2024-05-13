import pytest

import source.shapes as shapes
import math

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10,20)
# @pytest.fixture
# def another_same_rectangle():
#     return shapes.Rectangle(10,20)
# @pytest.fixture
# def another_rectangle():
#     return shapes.Rectangle(20,10)

def test_area(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    assert my_rectangle.area() == 10 * 20

def test_perimeter(rectangle_factory):
    my_rectangle = rectangle_factory(10, 20)
    assert my_rectangle.perimeter() == 10*2 + 20*2

def test_equality(rectangle_factory):
    my_rectangle = rectangle_factory(10, 20)
    another_same_rectangle = rectangle_factory(10, 20)
    assert my_rectangle == another_same_rectangle

def test_inequality(rectangle_factory):
    my_rectangle = rectangle_factory(10,20)
    another_rectangle = rectangle_factory(20,10)
    assert my_rectangle != another_rectangle