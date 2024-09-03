from db_connection import create_connection

class StudentManager:
    def __init__(self):
        self.connection = create_connection()

    def add_student(self, student_id, name, age, major, year):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Students (student_id, name, age, major, year) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (student_id, name, age, major, year))
            self.connection.commit()
            print("Student added successfully")
        except Exception as e:
            print(f"Failed to add student: {e}")

    def update_student(self, student_id, name, age, major, year):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Students SET name = %s, age = %s, major = %s, year = %s WHERE student_id = %s"
            cursor.execute(query, (name, age, major, year, student_id))
            self.connection.commit()
            print("Student updated successfully")
        except Exception as e:
            print(f"Failed to update student: {e}")

    def delete_student(self, student_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            self.connection.commit()
            print("Student deleted successfully")
        except Exception as e:
            print(f"Failed to delete student: {e}")
            
    def get_students_in_course(self, course_id):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT s.student_id, s.name
            FROM Students s
            JOIN Enrollments e ON s.student_id = e.student_id
            WHERE e.course_id = %s
            """
            cursor.execute(query, (course_id,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Failed to get students in course: {e}")
            return []