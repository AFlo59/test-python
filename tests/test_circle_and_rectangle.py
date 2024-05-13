import pytest
import source.shapes as shapes
import math
from tests.conftest import *


def test_area_inequality(rectangle_factory, circle_factory):
    this_rectangle = rectangle_factory(10,20)
    this_circle = circle_factory(15)
    assert this_rectangle.area() != this_circle.area()