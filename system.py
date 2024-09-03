from student import StudentManager
from course import CourseManager
from enrollment import EnrollmentManager

class StudentEnrollmentSystem:
    def __init__(self):
        self.student_manager = StudentManager()
        self.course_manager = CourseManager()
        self.enrollment_manager = EnrollmentManager()

    def add_student(self, student_id, name, age, major, year):
        self.student_manager.add_student(student_id, name, age, major, year)

    def update_student(self, student_id, name, age, major, year):
        self.student_manager.update_student(student_id, name, age, major, year)

    def delete_student(self, student_id):
        self.student_manager.delete_student(student_id)

    def add_course(self, course_id, course_name, credits):
        self.course_manager.add_course(course_id, course_name, credits)

    def update_course(self, course_id, course_name, credits):
        self.course_manager.update_course(course_id, course_name, credits)

    def delete_course(self, course_id):
        self.course_manager.delete_course(course_id)

    def enroll_student(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_manager.enroll_student(enrollment_id, student_id, course_id, enrollment_date)

    def drop_student(self, student_id, course_id):
        self.enrollment_manager.drop_student(student_id, course_id)

    def get_students_in_course(self, course_id):
        try:
            cursor = self.enrollment_manager.connection.cursor()
            query = """
            SELECT s.name
            FROM Students s
            JOIN Enrollments e ON s.student_id = e.student_id
            WHERE e.course_id = %s
            """
            cursor.execute(query, (course_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get students in course: {e}")
            return []

    def view_students_in_course(self, course_id):
        students = self.student_manager.get_students_in_course(course_id)
        if students:
            print(f"Students enrolled in course ID {course_id}:")
            for student in students:
                print(f"- {student[1]} (ID: {student[0]})")
        else:
            print("No students enrolled in this course.")