# Class: Course
class Course:
    # Constructor method with attributes: course_name, teacher
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    # Method: add_student
    def add_student(self, student):
        self.students.append(student)

    # Method: course_info
    def course_info(self):
        return f"Course: {self.course_name}, Teacher: {self.teacher.name}, Students Enrolled: {len(self.students)}"
