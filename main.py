"""main.py
Command-line interface using argparse for the Gradebook app.
"""


import argparse
from gradebook import service


def main():
    parser = argparse.ArgumentParser(
        prog="gradebook", description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add-student
    student_parser = subparsers.add_parser("add-student")
    student_parser.add_argument("--name", required=True)

    # add-course
    course_parser = subparsers.add_parser("add-course")
    course_parser.add_argument("--code", required=True)
    course_parser.add_argument("--title", required=True)

    # enroll
    enroll_parser = subparsers.add_parser("enroll")
    enroll_parser.add_argument("--student-id", type=int, required=True)
    enroll_parser.add_argument("--course-code", required=True)

    # add-grade
    grade_parser = subparsers.add_parser("add-grade")
    grade_parser.add_argument("--student-id", type=int, required=True)
    grade_parser.add_argument("--course-code", required=True)
    grade_parser.add_argument("--grade", type=float, required=True)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "entity", choices=["students", "courses", "enrollments"])

    # avg
    avg_parser = subparsers.add_parser("avg")
    avg_parser.add_argument("--student-id", type=int, required=True)
    avg_parser.add_argument("--course-code", required=True)

    # gpa
    gpa_parser = subparsers.add_parser("gpa")
    gpa_parser.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student = service.add_student(args.name)
            print(f"Added student: {student}")

        elif args.command == "add-course":
            course = service.add_course(args.code, args.title)
            print(f"Added course: {course}")

        elif args.command == "enroll":
            enrollment = service.enroll_student(
                args.student_id, args.course_code)
            print(f"Enrolled: {enrollment}")

        elif args.command == "add-grade":
            try:
                grade = service.parse_grade(args.grade)
                result = service.add_grade(
                    args.student_id, args.course_code, grade)
                print(f"Added grade: {result}")
            except ValueError as ve:
                print(f"Invalid grade: {ve}")

        elif args.command == "list":
            if args.entity == "students":
                for s in service.list_students():
                    print(f"ID: {s['id']} | Name: {s['name']}")
            elif args.entity == "courses":
                for c in service.list_courses():
                    print(f"Code: {c['code']} | Title: {c['title']}")
            else:
                for e in service.list_enrollments():
                    print(
                        f"StudentID: {e['student_id']} | Course: {e['course_code']} | Grades: {e['grades']}")

        elif args.command == "avg":
            avg = service.compute_average(args.student_id, args.course_code)
            if avg is None:
                print("No grades yet for this course.")
            else:
                print(
                    f"Average for student {args.student_id} in {args.course_code}: {avg}")

        elif args.command == "gpa":
            gpa = service.compute_gpa(args.student_id)
            print(f"GPA for student {args.student_id}: {gpa}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
