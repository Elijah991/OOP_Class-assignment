# Class: Student (inherits from Person)
class Student(Person):
    # Constructor method with attributes: name, age, student_id
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Method: study
    def study(self):
        return f"{self.name} is studying."
