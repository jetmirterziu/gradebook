"""gradebook/service.py
Implements business logic: add_student, add_course, enroll, add_grade, etc.
Includes logging and input validation helpers.
"""


import logging
import os
from gradebook.models import Student, Course, Enrollment
from gradebook.storage import load_data, save_data


# Configure logging
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add_student(name):

    data = load_data()
    new_id = len(data["students"]) + 1

    student = Student(new_id, name)
    data["students"].append(student.__dict__)
    save_data(data)
    logging.info(f"Added student: {student}")
    return student


def add_course(code, title):

    data = load_data()

    # Prevent duplicates
    for course in data["courses"]:
        if course["code"] == code:
            raise ValueError(f"Course with code '{code}' already exists.")

    course = Course(code, title)
    data["courses"].append(course.__dict__)
    save_data(data)
    logging.info(f"Added course: {course}")
    return course


def enroll_student(student_id, course_code):

    data = load_data()

    # Validate existence
    if not any(s["id"] == student_id for s in data["students"]):
        logging.error(f"Enrollment failed: Student ID {student_id} not found.")
        raise ValueError("Student not found.")

    if not any(c["code"] == course_code for c in data["courses"]):
        logging.error(
            f"Enrollment failed: Course code {course_code} not found.")
        raise ValueError("Course not found.")

    # Prevent duplicate enrollments
    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            logging.error(
                f"Enrollment failed: Student ID {student_id} already enrolled in course {course_code}.")
            raise ValueError("Student already enrolled in this course.")

    enrollment = Enrollment(student_id, course_code)
    data["enrollments"].append(enrollment.__dict__)
    save_data(data)
    logging.info(f"Enrolled student {student_id} in course {course_code}")
    return enrollment


def add_grade(student_id, course_code, grade):

    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:

            if not (0 <= grade <= 100):
                raise ValueError("Grade must be between 0 and 100.")

            e["grades"].append(grade)
            save_data(data)
            return e

    raise ValueError("Enrollment not found.")


def list_students():

    data = load_data()
    return sorted(
        [s for s in data["students"]],
        key=lambda s: s["name"].lower()
    )


def list_courses():

    data = load_data()
    return sorted(
        [c for c in data["courses"]],
        key=lambda c: c["code"].lower()
    )


def list_enrollments():

    data = load_data()

    return sorted(
        [e for e in data["enrollments"]],
        key=lambda e: (e["student_id"], e["course_code"])
    )


def compute_average(student_id, course_code):

    data = load_data()

    for e in data["enrollments"]:
        if e["student_id"] == student_id and e["course_code"] == course_code:
            grades = e.get("grades", [])
            if not grades:
                return None
            return round(sum(grades) / len(grades), 2)
    raise ValueError("Enrollment not found.")


def compute_gpa(student_id):

    data = load_data()
    enrollments = [e for e in data["enrollments"]
                   if e["student_id"] == student_id]

    if not enrollments:
        raise ValueError("Student not enrolled in any courses.")

    averages = []
    for e in enrollments:
        if e["grades"]:
            avg = sum(e["grades"]) / len(e["grades"])
            averages.append(avg)

    return round(sum(averages) / len(averages), 2) if averages else None


def parse_grade(value):

    try:
        grade = float(value)
    except ValueError:
        raise ValueError("Grade must be a number.")
    if not (0 <= grade <= 100):
        raise ValueError("Grade must be between 0 and 100.")
    return grade
