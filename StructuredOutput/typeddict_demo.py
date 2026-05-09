from typing import TypedDict

class Person(TypedDict):
    id: int
    name: str
    email: str



new_person = Person(id=1, name="John Doe", email="john.doe@example.com")