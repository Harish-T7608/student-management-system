students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")

    students.append({
        "name": name,
        "roll_no": roll_no,
        "department": department
    })

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for student in students:
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Department:", student["department"])
        print("--------------------")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
