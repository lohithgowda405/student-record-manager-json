
import json
import os

FILE = "students.json"


# ---------- Load Students ----------
def load_students():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


# ---------- Save Students ----------
def save_students(students):

    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)


# ---------- Add Student ----------
def add_student():

    students = load_students()

    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    marks = float(input("Enter Marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    save_students(students)

    print("✅ Student Added Successfully")


# ---------- View Students ----------
def view_students():

    students = load_students()

    if not students:
        print("No Records Found")
        return

    print("\nStudent Records")

    for s in students:

        print(
            f"Name:{s['name']} | Roll:{s['roll']} | Marks:{s['marks']}"
        )


# ---------- Search Student ----------
def search_student():

    roll = input("Enter Roll Number: ")

    students = load_students()

    for s in students:

        if s["roll"] == roll:

            print(
                f"Found -> {s['name']} Marks:{s['marks']}"
            )
            return

    print("Student Not Found")


# ---------- Average Marks ----------
def average_marks():

    students = load_students()

    if not students:
        print("No Data")
        return

    total = sum(s["marks"] for s in students)

    avg = total / len(students)

    print("Average Marks =", avg)


# ---------- Topper ----------
def topper():

    students = load_students()

    if not students:
        print("No Records")
        return

    top = max(students,
              key=lambda x: x["marks"])

    print(
        f"Topper -> {top['name']} ({top['marks']})"
    )


# ---------- Menu ----------
def menu():

    while True:

        print("\n==== Student Manager ====")

        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Average Marks")
        print("5 Topper")
        print("6 Exit")

        choice = input("Enter Choice:")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            average_marks()

        elif choice == "5":
            topper()

        elif choice == "6":
            print("Exit...")
            break

        else:
            print("Invalid Choice")


menu()