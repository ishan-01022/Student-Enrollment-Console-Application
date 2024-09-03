from system import StudentEnrollmentSystem
from datetime import datetime

def main():
    system = StudentEnrollmentSystem()

    while True:
        print("\nStudent Enrollment System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. Update Course")
        print("6. Delete Course")
        print("7. Enroll Student")
        print("8. Drop Student")
        print("9. View Students in Course")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            major = input("Enter Major: ")
            year = input("Enter Year: ")
            system.add_student(student_id, name, age, major, year)

        elif choice == '2':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            major = input("Enter Major: ")
            year = input("Enter Year: ")
            system.update_student(student_id, name, age, major, year)

        elif choice == '3':
            student_id = int(input("Enter Student ID: "))
            system.delete_student(student_id)

        elif choice == '4':
            course_id = int(input("Enter Course ID: "))
            course_name = input("Enter Course Name: ")
            credits = int(input("Enter Credits: "))
            system.add_course(course_id, course_name, credits)

        elif choice == '5':
            course_id = int(input("Enter Course ID: "))
            course_name = input("Enter Course Name: ")
            credits = int(input("Enter Credits: "))
            system.update_course(course_id, course_name, credits)

        elif choice == '6':
            course_id = int(input("Enter Course ID: "))
            system.delete_course(course_id)

        elif choice == '7':
            enrollment_id = int(input("Enter Enrollment ID: "))
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            enrollment_date = datetime.now().date()
            system.enroll_student(enrollment_id, student_id, course_id, enrollment_date)

        elif choice == '8':
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            system.drop_student(student_id, course_id)

        elif choice == '9':
            course_id = int(input("Enter Course ID: "))
            students = system.get_students_in_course(course_id)
            print("Students enrolled in course:")
            for student in students:
                print(student[0])

        elif choice == '10':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
