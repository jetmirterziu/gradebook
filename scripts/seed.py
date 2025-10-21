"""scripts/seed.py
Populate the gradebook with sample data for quick testing or demonstration.
"""

from gradebook import service, storage
import os
import sys

# Ensure we can import the package from one directory up
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def seed_data():
    """Add example students, courses, enrollments, and grades."""
    print("Seeding data...")

    # Reset data to a clean state
    storage.save_data({"students": [], "courses": [], "enrollments": []})

    # --- Add students ---
    students = [
        service.add_student("Alice Johnson"),
        service.add_student("Bob Smith"),
        service.add_student("Carol White"),
    ]

    # --- Add courses ---
    courses = [
        service.add_course("CS101", "Introduction to Computer Science"),
        service.add_course("MATH101", "Mathematics I"),
        service.add_course("PHY101", "Physics Basics"),
    ]

    # --- Enroll students ---
    service.enroll_student(students[0].id, courses[0].code)
    service.enroll_student(students[0].id, courses[1].code)
    service.enroll_student(students[1].id, courses[0].code)
    service.enroll_student(students[2].id, courses[2].code)

    # --- Add grades ---
    service.add_grade(students[0].id, courses[0].code, 95)
    service.add_grade(students[0].id, courses[0].code, 85)
    service.add_grade(students[0].id, courses[1].code, 75)
    service.add_grade(students[1].id, courses[0].code, 88)
    service.add_grade(students[2].id, courses[2].code, 92)

    print("✅ Seed data added successfully!")


if __name__ == "__main__":
    seed_data()
