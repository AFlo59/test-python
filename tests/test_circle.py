import pytest

import source.shapes as shapes
import math

# class TestCircle:
#     def setup_method(self):
#         self.circle = shapes.Circle(10)

#     def test_area(self):
#         assert self.circle.area() == math.pi * self.circle.radius ** 2

#     def test_perimeter(self):
#         assert self.circle.perimeter() == math.pi * self.circle.radius * 2

def test_area(circle_factory):
    my_circle = circle_factory(10)
    assert my_circle.area() == math.pi * my_circle.radius ** 2

def test_perimeter(circle_factory):
    my_circle = circle_factory(10)
    assert my_circle.perimeter() == math.pi * my_circle.radius * 2