from database import Database
from user import User
from student import Student
from getpass import getpass


class StudentRegistrationSystem:
    
    def __init__(self):
        print("="*60)
        print("   STUDENT REGISTRATION SYSTEM - MVP")
        print("="*60)
        
        self.db = Database(
            host='localhost',
            user='root',
            password='databasepwd123',
            database='student_db'
        )
        
        if not self.db.connect():
            print("\n✗ Failed to connect to database!")
            print("Check:")
            print("  1. MySQL server is running")
            print("  2. Database 'student_db' exists")
            print("  3. Connection parameters are correct")
            exit(1)
        
        self.user = User(self.db)
        self.student = Student(self.db)
    
    def display_main_menu(self):
        print("\n" + "="*60)
        print("   MAIN MENU")
        print("="*60)
        print("1. User Registration")
        print("2. Login")
        print("3. Exit")
        print("="*60)
    
    def display_student_menu(self):
        print("\n" + "="*60)
        print("   STUDENT MANAGEMENT")
        print("="*60)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Find Student by ID")
        print("4. Update Student Data")
        print("5. Delete Student")
        print("6. Search Students")
        print("7. Logout")
        print("="*60)
    
    def run(self):
        while True:
            if not self.user.is_logged_in():
                self.display_main_menu()
                choice = input("\nSelect action (1-3): ").strip()
                
                if choice == '1':
                    self.handle_registration()
                elif choice == '2':
                    self.handle_login()
                elif choice == '3':
                    print("\n✓ Exiting application...")
                    break
                else:
                    print("\n✗ Invalid choice! Try again.")
            else:
                self.display_student_menu()
                choice = input("\nSelect action (1-7): ").strip()
                
                if choice == '1':
                    self.handle_add_student()
                elif choice == '2':
                    print("\n[View All Students]")
                    print("TODO: Will be implemented in next sessions")
                elif choice == '3':
                    self.handle_find_student_by_id()
                elif choice == '4':
                    print("\n[Update Student Data]")
                    print("TODO: Will be implemented in next sessions")
                elif choice == '5':
                    print("\n[Delete Student]")
                    print("TODO: Will be implemented in next sessions")
                elif choice == '6':
                    print("\n[Search Students]")
                    print("TODO: Will be implemented in next sessions")
                elif choice == '7':
                    self.user.logout()
                    print("\n✓ You have logged out")
                else:
                    print("\n✗ Invalid choice! Try again.")
    
    def handle_registration(self):
        print("\n" + "="*60)
        print("   USER REGISTRATION")
        print("="*60)
        
        username = input("Enter username: ").strip()
        
        if not username:
            print("\n✗ Username cannot be empty!")
            return
        
        password = getpass("Enter password: ")
        
        if not password:
            print("\n✗ Password cannot be empty!")
            return
        
        confirm_password = getpass("Confirm password: ")
        
        if password != confirm_password:
            print("\n✗ Passwords do not match!")
            return
        
        self.user.register(username, password)
    
    def handle_login(self):
        print("\n" + "="*60)
        print("   USER LOGIN")
        print("="*60)
        
        username = input("Enter username: ").strip()
        password = getpass("Enter password: ")
        
        self.user.login(username, password)
    
    def handle_add_student(self):
        print("\n" + "="*60)
        print("   ADD NEW STUDENT")
        print("="*60)
        
        name = input("Enter student name: ").strip()
        
        if not name:
            print("\n✗ Name cannot be empty!")
            return
        
        try:
            age = int(input("Enter student age: ").strip())
        except ValueError:
            print("\n✗ Age must be a number!")
            return
        
        course = input("Enter course name: ").strip()
        
        if not course:
            print("\n✗ Course cannot be empty!")
            return
        
        email = input("Enter student email: ").strip()
        
        if not email:
            print("\n✗ Email cannot be empty!")
            return
        
        self.student.add_student(name, age, course, email)
    
    def handle_find_student_by_id(self):
        print("\n" + "="*60)
        print("   FIND STUDENT BY ID")
        print("="*60)
        
        try:
            student_id = int(input("Enter student ID: ").strip())
        except ValueError:
            print("\n✗ Student ID must be a number!")
            return
        
        self.student.view_student_by_id(student_id)
    
    def cleanup(self):
        self.db.disconnect()


def main():
    system = StudentRegistrationSystem()
    
    try:
        system.run()
    except KeyboardInterrupt:
        print("\n\n✓ Interrupted by user")
    except Exception as e:
        print(f"\n✗ An error occurred: {e}")
    finally:
        system.cleanup()
        print("\n✓ Finished. Goodbye!")


if __name__ == "__main__":
    main()

