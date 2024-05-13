import pytest
from source.contact import Contact

@pytest.fixture
def contact_factory():
    def create_contact(name, age):
        return Contact(name=name, age=age)
    return create_contact

def test_contact_greeting(contact_factory):
    contact = contact_factory("Jhon Doe", 30)
    assert contact.greet() == "Hello, my name is Jhon Doe and I am 30 years old."

def test_contact_underage(contact_factory):
    contact = contact_factory("Jane Doe", 17)
    assert contact.age < 18

def test_contact_adulte(contact_factory):
    contact = contact_factory("Bob Doe", 21)
    assert contact.age >= 18