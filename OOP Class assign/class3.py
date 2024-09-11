# Class: Teacher (inherits from Person)
class Teacher(Person):
    # Constructor method with attributes: name, age, subject
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Method: teach
    def teach(self):
        return f"{self.name} is teaching {self.subject}."
