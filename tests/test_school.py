import pytest
from source.school import Student, Course

def test_course(course_factory, student_factory):
    course = course_factory(101, "Math")
    student = student_factory(1, "Jhon Doe")

    course.add_student(student)
    assert course.student_count() == 1
    assert student in course.students

def test_course_two(course_factory, student_factory):
    course = course_factory(102, "physic")
    student1 = student_factory(1, "Jhon Doe")
    student2 = student_factory(2, "Lee Doe")
    students = [student1, student2]

    for student in students:
        course.add_student(student)

    assert course.student_count() == 2 