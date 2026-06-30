import os

FILE_NAME = "students.txt"

# Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{dept}\n")

    print("Student Added Successfully!\n")


# View Students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No Records Found.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No Records Found.\n")
        return

    print("\nStudent Records")
    print("-" * 40)

    for line in data:
        roll, name, dept = line.strip().split(",")
        print(f"Roll : {roll}")
        print(f"Name : {name}")
        print(f"Dept : {dept}")
        print("-" * 40)


# Search Student
def search_student():
    roll_no = input("Enter Roll No to Search: ")

    if not os.path.exists(FILE_NAME):
        print("No Records Found.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, dept = line.strip().split(",")

            if roll == roll_no:
                print("\nStudent Found")
                print("-------------")
                print("Roll :", roll)
                print("Name :", name)
                print("Department :", dept)
                found = True
                break

    if not found:
        print("Student Not Found.\n")


# Delete Student
def delete_student():
    roll_no = input("Enter Roll No to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No Records Found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in records:
            roll, name, dept = line.strip().split(",")

            if roll != roll_no:
                file.write(line)
            else:
                found = True

    if found:
        print("Student Deleted Successfully.\n")
    else:
        print("Student Not Found.\n")


# Main Menu
while True:

    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
