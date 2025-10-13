class Student:
    
    def __init__(self, database):
        self.database = database
    
    def add_student(self, name, age, course, email):

        if not name or not name.strip():
            print("\n✗ Name cannot be empty!")
            return False
        
        if not isinstance(age, int) or age <= 0:
            print("\n✗ Age must be a positive number!")
            return False
        
        if not course or not course.strip():
            print("\n✗ Course cannot be empty!")
            return False
        
        if not email or not email.strip():
            print("\n✗ Email cannot be empty!")
            return False
        
        if '@' not in email or '.' not in email:
            print("\n✗ Invalid email format!")
            return False
        
        check_query = "SELECT * FROM students WHERE email = %s"
        existing = self.database.fetch_query(check_query, (email,))
        
        if existing:
            print(f"\n✗ Student with email '{email}' already exists!")
            return False
        
        insert_query = """
        INSERT INTO students (name, age, course, email)
        VALUES (%s, %s, %s, %s)
        """
        
        if self.database.execute_query(insert_query, (name, age, course, email)):
            print(f"\n✓ Student '{name}' added successfully!")
            return True
        else:
            print("\n✗ Failed to add student!")
            return False
    
    def view_all_students(self):
        pass
    
    def view_student_by_id(self, student_id):
        """
        Retrieves a student record by their ID
        Args:
            student_id: The unique ID of the student
        Returns:
            Student record dictionary or None if not found
        """
        if not isinstance(student_id, int) or student_id <= 0:
            print("\n✗ Student ID must be a positive number!")
            return None
        
        query = "SELECT * FROM students WHERE student_id = %s"
        result = self.database.fetch_query(query, (student_id,))
        
        if result and len(result) > 0:
            student = result[0]
            print("\n" + "="*60)
            print("   STUDENT DETAILS")
            print("="*60)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Course     : {student['course']}")
            print(f"Email      : {student['email']}")
            print("="*60)
            return student
        else:
            print(f"\n✗ Student with ID '{student_id}' not found!")
            return None
    
    def update_student(self, student_id, name=None, age=None, course=None, email=None):
        pass
    
    def delete_student(self, student_id):
        pass
    
    def search_students(self, search_term):
        pass

