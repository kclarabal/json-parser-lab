import json
from pathlib import Path


def load_json_file(file_path):
    """
    Loads and parses a JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return None


def display_school_info(data):
    """
    Displays general school and semester information.
    """
    print("=" * 60)
    print("SCHOOL ENROLLMENT DATA")
    print("=" * 60)
    print(f"School: {data['school']}")
    print(f"Semester: {data['semester']}")
    print(f"Academic Year: {data['academic_year']}")
    print("=" * 60)


def calculate_total_units(courses):
    """
    Calculates the total number of units from a list of courses.
    """
    total_units = 0

    for course in courses:
        total_units += course["units"]

    return total_units


def display_students(data):
    """
    Displays student information and enrolled courses.
    """
    students = data["students"]

    for student in students:
        full_name = f"{student['first_name']} {student['last_name']}"
        courses = student["courses"]
        total_units = calculate_total_units(courses)

        print()
        print(f"Student ID: {student['student_id']}")
        print(f"Name: {full_name}")
        print(f"Program: {student['program']}")
        print(f"Year Level: {student['year_level']}")
        print(f"Email: {student['email']}")
        print(f"Total Enrolled Units: {total_units}")
        print("Courses:")

        for course in courses:
            print(
                f"  - {course['course_code']}: "
                f"{course['course_title']} "
                f"({course['units']} units) | Instructor: {course['instructor']}"
            )


def display_summary(data):
    """
    Displays a summary report of all students.
    """
    students = data["students"]
    total_students = len(students)
    total_courses = sum(len(s["courses"]) for s in students)
    total_units_all = sum(calculate_total_units(s["courses"]) for s in students)
    avg_units = total_units_all / total_students if total_students > 0 else 0

    bs_it_students = [s for s in students if s["program"] == "BS Information Technology"]

    print()
    print("=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    print(f"Total Students: {total_students}")
    print(f"Total Courses Enrolled: {total_courses}")
    print(f"Average Units Per Student: {avg_units:.2f}")
    print()
    print("BS Information Technology Students:")
    for s in bs_it_students:
        print(f"  - {s['first_name']} {s['last_name']}")


def main():
    """
    Main program function.
    """
    json_file_path = Path("data/students.json")

    data = load_json_file(json_file_path)

    if data is not None:
        display_school_info(data)
        display_students(data)
        display_summary(data)


if __name__ == "__main__":
    main()