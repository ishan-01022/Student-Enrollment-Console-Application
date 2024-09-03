from db_connection import create_connection

class CourseManager:
    def __init__(self):
        self.connection = create_connection()

    def add_course(self, course_id, course_name, credits):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Courses (course_id, course_name, credits) VALUES (%s, %s, %s)"
            cursor.execute(query, (course_id, course_name, credits))
            self.connection.commit()
            print("Course added successfully")
        except Exception as e:
            print(f"Failed to add course: {e}")

    def update_course(self, course_id, course_name, credits):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Courses SET course_name = %s, credits = %s WHERE course_id = %s"
            cursor.execute(query, (course_name, credits, course_id))
            self.connection.commit()
            print("Course updated successfully")
        except Exception as e:
            print(f"Failed to update course: {e}")

    def delete_course(self, course_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Courses WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            self.connection.commit()
            print("Course deleted successfully")
        except Exception as e:
            print(f"Failed to delete course: {e}")
