"""gradebook/models.py
Defines the core data models: Student, Course, Enrollment.
"""


class Student:

    def __init__(self, id, name):

        if not isinstance(id, int) or id <= 0:
            raise ValueError("Student ID must be a positive integer.")

        if not name or not isinstance(name, str):
            raise ValueError("Student name must be a non-empty string.")

        self.id = id
        self.name = name

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course:

    def __init__(self, code, title):

        if not code or not isinstance(code, str):
            raise ValueError("Course code must be a non-empty string.")

        if not title or not isinstance(title, str):
            raise ValueError("Course title must be a non-empty string.")

        self.code = code
        self.title = title

    def __str__(self):
        return f"Course(code='{self.code}', title='{self.title}')"


class Enrollment:

    def __init__(self, student_id, course_code, grades=None):

        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student ID must be a positive integer.")

        if not course_code or not isinstance(course_code, str):
            raise ValueError("Course code must be a non-empty string.")

        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

        for grade in self.grades:
            if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
                raise ValueError(
                    f"Invalid grade '{grade}'. Grades must be between 0 and 100.")

    def __str__(self):
        return f"Enrollment(student_id={self.student_id}, course_code='{self.course_code}', grades={self.grades})"
