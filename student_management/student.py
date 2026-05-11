class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print("-" * 25)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(roll_no, name, marks)
        self.students.append(student)

        print("Student added successfully!\n")

    # View all students
    def view_students(self):
        if not self.students:
            print("No students found.\n")
            return

        print("\n--- Student Records ---")
        for student in self.students:
            student.display()

    # Search student
    def search_student(self):
        roll_no = input("Enter Roll Number to Search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display()
                return

        print("Student not found.\n")

    # Delete student
    def delete_student(self):
        roll_no = input("Enter Roll Number to Delete: ")

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return

        print("Student not found.\n")


# Main Program
sms = StudentManagementSystem()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        sms.add_student()

    elif choice == '2':
        sms.view_students()

    elif choice == '3':
        sms.search_student()

    elif choice == '4':
        sms.delete_student()

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")