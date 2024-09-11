# Class: Person
class Person:
    # Constructor method with attributes: name, age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method: introduce
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
