from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class Student:
    
    def __init__(self, database):
        self.database = database
    
    def add_student(self, name, age, course, email):
        if not name or not name.strip():
            console.print("\n[red]✗ Name cannot be empty![/red]")
            return False
        
        if not isinstance(age, int) or age <= 0:
            console.print("\n[red]✗ Age must be a positive number![/red]")
            return False
        
        if not course or not course.strip():
            console.print("\n[red]✗ Course cannot be empty![/red]")
            return False
        
        if not email or not email.strip():
            console.print("\n[red]✗ Email cannot be empty![/red]")
            return False
        
        if '@' not in email or '.' not in email:
            console.print("\n[red]✗ Invalid email format![/red]")
            return False
        
        check_query = "SELECT * FROM students WHERE email = %s"
        existing = self.database.fetch_query(check_query, (email,))
        
        if existing:
            console.print(f"\n[red]✗ Student with email '{email}' already exists![/red]")
            return False
        
        insert_query = """
        INSERT INTO students (name, age, course, email)
        VALUES (%s, %s, %s, %s)
        """
        
        if self.database.execute_query(insert_query, (name, age, course, email)):
            console.print(f"\n[green]✓ Student '{name}' added successfully![/green]")
            return True
        else:
            console.print("\n[red]✗ Failed to add student![/red]")
            return False
    
    def view_all_students(self):
        pass
    
    def view_student_by_id(self, student_id):
        if not isinstance(student_id, int) or student_id <= 0:
            console.print("\n[red]✗ Student ID must be a positive number![/red]")
            return None
        
        query = "SELECT * FROM students WHERE student_id = %s"
        result = self.database.fetch_query(query, (student_id,))
        
        if result and len(result) > 0:
            student = result[0]
            
            table = Table(title="STUDENT DETAILS", show_header=False, border_style="cyan")
            table.add_column("Field", style="bold cyan", width=15)
            table.add_column("Value", style="white")
            
            table.add_row("Student ID", str(student['student_id']))
            table.add_row("Name", student['name'])
            table.add_row("Age", str(student['age']))
            table.add_row("Course", student['course'])
            table.add_row("Email", student['email'])
            
            console.print()
            console.print(table)
            return student
        else:
            console.print(f"\n[red]✗ Student with ID '{student_id}' not found![/red]")
            return None
    
    def update_student(self, student_id, name=None, age=None, course=None, email=None):
        if not isinstance(student_id, int) or student_id <= 0:
            console.print("\n[red]✗ Student ID must be a positive number![/red]")
            return False
        
        check_query = "SELECT * FROM students WHERE student_id = %s"
        existing = self.database.fetch_query(check_query, (student_id,))
        
        if not existing or len(existing) == 0:
            console.print(f"\n[red]✗ Student with ID '{student_id}' not found![/red]")
            return False
        
        update_fields = []
        update_values = []
        
        if name and name.strip():
            update_fields.append("name = %s")
            update_values.append(name.strip())
        
        if age is not None:
            if not isinstance(age, int) or age <= 0:
                console.print("\n[red]✗ Age must be a positive number![/red]")
                return False
            update_fields.append("age = %s")
            update_values.append(age)
        
        if course and course.strip():
            update_fields.append("course = %s")
            update_values.append(course.strip())
        
        if email and email.strip():
            if '@' not in email or '.' not in email:
                console.print("\n[red]✗ Invalid email format![/red]")
                return False
            
            email_check_query = "SELECT * FROM students WHERE email = %s AND student_id != %s"
            email_exists = self.database.fetch_query(email_check_query, (email, student_id))
            
            if email_exists:
                console.print(f"\n[red]✗ Email '{email}' is already used by another student![/red]")
                return False
            
            update_fields.append("email = %s")
            update_values.append(email.strip())
        
        if not update_fields:
            console.print("\n[red]✗ No fields provided to update![/red]")
            return False
        
        update_query = f"UPDATE students SET {', '.join(update_fields)} WHERE student_id = %s"
        update_values.append(student_id)
        
        if self.database.execute_query(update_query, tuple(update_values)):
            console.print(f"\n[green]✓ Student with ID '{student_id}' updated successfully![/green]")
            return True
        else:
            console.print("\n[red]✗ Failed to update student![/red]")
            return False
    
    def delete_student(self, student_id):
        pass
    
    def search_students(self, search_term):
        pass
