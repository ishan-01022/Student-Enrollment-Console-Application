import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Ishan@0102',
            database='student_enrollment'
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
