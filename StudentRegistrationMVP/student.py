class Student:
    
    def __init__(self, database):
        self.database = database
    
    def add_student(self, name, age, course, email):
        # Validate input
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
        
        # Basic email validation
        if '@' not in email or '.' not in email:
            print("\n✗ Invalid email format!")
            return False
        
        # Check if email already exists
        check_query = "SELECT * FROM students WHERE email = %s"
        existing = self.database.fetch_query(check_query, (email,))
        
        if existing:
            print(f"\n✗ Student with email '{email}' already exists!")
            return False
        
        # Insert student into database
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
        pass
    
    def update_student(self, student_id, name=None, age=None, course=None, email=None):
        pass
    
    def delete_student(self, student_id):
        pass
    
    def search_students(self, search_term):
        pass

