import mysql.connector
from mysql.connector import Error


class Database:
    
    def __init__(self, host='localhost', user='root', password='', database='student_db'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print(f"✓ Successfully connected to database '{self.database}'")
                return True
        except Error as e:
            print(f"✗ Database connection error: {e}")
            return False
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("✓ Database connection closed")
    
    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            print(f"✗ Query execution error: {e}")
            return False
    
    def fetch_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"✗ Query execution error: {e}")
            return None
    
    def create_tables(self):
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(64) NOT NULL
        )
        """
        
        create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """
        
        success = True
        
        if self.execute_query(create_users_table):
            print("✓ Table 'users' created successfully")
        else:
            print("✗ Failed to create 'users' table")
            success = False
        
        if self.execute_query(create_students_table):
            print("✓ Table 'students' created successfully")
        else:
            print("✗ Failed to create 'students' table")
            success = False
        
        return success

