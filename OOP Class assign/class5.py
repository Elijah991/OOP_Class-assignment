class School:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def school_info(self):
        return f"School: {self.name}, Number of Courses: {len(self.courses)}"
