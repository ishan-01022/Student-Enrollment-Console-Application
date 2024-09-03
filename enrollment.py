from db_connection import create_connection

class EnrollmentManager:
    def __init__(self):
        self.connection = create_connection()

    def enroll_student(self, enrollment_id, student_id, course_id, enrollment_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (enrollment_id, student_id, course_id, enrollment_date))
            self.connection.commit()
            print("Student enrolled successfully")
        except Exception as e:
            print(f"Failed to enroll student: {e}")

    def drop_student(self, student_id, course_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Enrollments WHERE student_id = %s AND course_id = %s"
            cursor.execute(query, (student_id, course_id))
            self.connection.commit()
            print("Student dropped from course successfully")
        except Exception as e:
            print(f"Failed to drop student: {e}")
