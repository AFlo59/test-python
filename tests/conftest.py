import pytest
import source.shapes as shapes
from source.contact import Contact
from source.school import Student, Course

# @pytest.fixture
# def this_rectangle():
#     return shapes.Rectangle(10,20)

# @pytest.fixture
# def this_circle():
#     return shapes.Circle(15)

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10,20)
# @pytest.fixture
# def another_same_rectangle():
#     return shapes.Rectangle(10,20)
# @pytest.fixture
# def another_rectangle():
#     return shapes.Rectangle(20,10)


@pytest.fixture
def contact_factory():
    def create_contact(name, age):
        return Contact(name=name, age=age)
    return create_contact

@pytest.fixture
def rectangle_factory():
    def create_rectangle(lenght, width):
        return shapes.Rectangle(lenght=lenght, width=width)
    return create_rectangle

@pytest.fixture
def circle_factory():
    def create_circle(radius):
        return shapes.Circle(radius=radius)
    return create_circle

@pytest.fixture
def student_factory():
    def create_student(student_id, name):
        return Student(student_id=student_id, name=name)
    return create_student

@pytest.fixture
def course_factory():
    def create_course(course_id, title):
        return Course(course_id=course_id, title=title)
    return create_course