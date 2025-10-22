from database import Database
from user import User
from student import Student
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()


class StudentRegistrationSystem:
    
    def __init__(self):
        console.print(Panel.fit(
            "[bold cyan]STUDENT REGISTRATION SYSTEM - MVP[/bold cyan]",
            border_style="cyan"
        ))
        
        self.db = Database(
            host='localhost',
            user='root',
            password='databasepwd123',
            database='student_db'
        )
        
        if not self.db.connect():
            console.print("\n[red]✗ Failed to connect to database![/red]")
            console.print("[yellow]Check:[/yellow]")
            console.print("  [yellow]1. MySQL server is running[/yellow]")
            console.print("  [yellow]2. Database 'student_db' exists[/yellow]")
            console.print("  [yellow]3. Connection parameters are correct[/yellow]")
            exit(1)
        
        self.user = User(self.db)
        self.student = Student(self.db)
    
    def display_main_menu(self):
        table = Table(title="\n[bold cyan]MAIN MENU[/bold cyan]", show_header=False, border_style="cyan")
        table.add_column("Option", style="bold yellow", width=5)
        table.add_column("Action", style="white")
        
        table.add_row("1.", "User Registration")
        table.add_row("2.", "Login")
        table.add_row("3.", "Exit")
        
        console.print(table)
    
    def display_student_menu(self):
        table = Table(title="\n[bold cyan]STUDENT MANAGEMENT[/bold cyan]", show_header=False, border_style="cyan")
        table.add_column("Option", style="bold yellow", width=5)
        table.add_column("Action", style="white")
        
        table.add_row("1.", "Add Student")
        table.add_row("2.", "View All Students")
        table.add_row("3.", "Find Student by ID")
        table.add_row("4.", "Update Student Data")
        table.add_row("5.", "Delete Student")
        table.add_row("6.", "Search Students")
        table.add_row("7.", "Logout")
        
        console.print(table)
    
    def run(self):
        while True:
            if not self.user.is_logged_in():
                self.display_main_menu()
                choice = Prompt.ask("\n[bold yellow]Select action[/bold yellow]", choices=["1", "2", "3"])
                
                if choice == '1':
                    self.handle_registration()
                elif choice == '2':
                    self.handle_login()
                elif choice == '3':
                    console.print("\n[green]✓ Exiting application...[/green]")
                    break
            else:
                self.display_student_menu()
                choice = Prompt.ask("\n[bold yellow]Select action[/bold yellow]", choices=["1", "2", "3", "4", "5", "6", "7"])
                
                if choice == '1':
                    self.handle_add_student()
                elif choice == '2':
                    self.handle_view_all_students()
                elif choice == '3':
                    self.handle_find_student_by_id()
                elif choice == '4':
                    self.handle_update_student()
                elif choice == '5':
                    console.print(Panel("[yellow]TODO: Will be implemented in next sessions[/yellow]", title="Delete Student", border_style="yellow"))
                elif choice == '6':
                    console.print(Panel("[yellow]TODO: Will be implemented in next sessions[/yellow]", title="Search Students", border_style="yellow"))
                elif choice == '7':
                    self.user.logout()
    
    def handle_registration(self):
        console.print(Panel.fit("[bold cyan]USER REGISTRATION[/bold cyan]", border_style="cyan"))
        
        username = Prompt.ask("\n[cyan]Enter username[/cyan]").strip()
        
        if not username:
            console.print("\n[red]✗ Username cannot be empty![/red]")
            return
        
        password = getpass("Enter password: ")
        
        if not password:
            console.print("\n[red]✗ Password cannot be empty![/red]")
            return
        
        confirm_password = getpass("Confirm password: ")
        
        if password != confirm_password:
            console.print("\n[red]✗ Passwords do not match![/red]")
            return
        
        self.user.register(username, password)
    
    def handle_login(self):
        console.print(Panel.fit("[bold cyan]USER LOGIN[/bold cyan]", border_style="cyan"))
        
        username = Prompt.ask("\n[cyan]Enter username[/cyan]").strip()
        password = getpass("Enter password: ")
        
        self.user.login(username, password)
    
    def handle_add_student(self):
        console.print(Panel.fit("[bold cyan]ADD NEW STUDENT[/bold cyan]", border_style="cyan"))
        
        name = Prompt.ask("\n[cyan]Enter student name[/cyan]").strip()
        
        if not name:
            console.print("\n[red]✗ Name cannot be empty![/red]")
            return
        
        try:
            age = int(Prompt.ask("[cyan]Enter student age[/cyan]").strip())
        except ValueError:
            console.print("\n[red]✗ Age must be a number![/red]")
            return
        
        course = Prompt.ask("[cyan]Enter course name[/cyan]").strip()
        
        if not course:
            console.print("\n[red]✗ Course cannot be empty![/red]")
            return
        
        email = Prompt.ask("[cyan]Enter student email[/cyan]").strip()
        
        if not email:
            console.print("\n[red]✗ Email cannot be empty![/red]")
            return
        
        self.student.add_student(name, age, course, email)
    
    def handle_find_student_by_id(self):
        console.print(Panel.fit("[bold cyan]FIND STUDENT BY ID[/bold cyan]", border_style="cyan"))
        
        try:
            student_id = int(Prompt.ask("\n[cyan]Enter student ID[/cyan]").strip())
        except ValueError:
            console.print("\n[red]✗ Student ID must be a number![/red]")
            return
        
        self.student.view_student_by_id(student_id)
    
    def handle_update_student(self):
        console.print(Panel.fit("[bold cyan]UPDATE STUDENT DATA[/bold cyan]", border_style="cyan"))
        
        try:
            student_id = int(Prompt.ask("\n[cyan]Enter student ID[/cyan]").strip())
        except ValueError:
            console.print("\n[red]✗ Student ID must be a number![/red]")
            return
        
        check_query = "SELECT * FROM students WHERE student_id = %s"
        existing = self.db.fetch_query(check_query, (student_id,))
        
        if not existing or len(existing) == 0:
            console.print(f"\n[red]✗ Student with ID '{student_id}' not found![/red]")
            return
        
        student = existing[0]
        
        table = Table(title="CURRENT STUDENT DETAILS", show_header=False, border_style="yellow")
        table.add_column("Field", style="bold yellow", width=10)
        table.add_column("Value", style="white")
        
        table.add_row("Name", student['name'])
        table.add_row("Age", str(student['age']))
        table.add_row("Course", student['course'])
        table.add_row("Email", student['email'])
        
        console.print()
        console.print(table)
        console.print("\n[dim]Leave field blank to keep current value[/dim]\n")
        
        name = Prompt.ask(f"[cyan]Enter new name (current: {student['name']})[/cyan]", default="").strip()
        
        age_input = Prompt.ask(f"[cyan]Enter new age (current: {student['age']})[/cyan]", default="").strip()
        age = None
        if age_input:
            try:
                age = int(age_input)
            except ValueError:
                console.print("\n[red]✗ Age must be a number! Skipping age update.[/red]")
        
        course = Prompt.ask(f"[cyan]Enter new course (current: {student['course']})[/cyan]", default="").strip()
        email = Prompt.ask(f"[cyan]Enter new email (current: {student['email']})[/cyan]", default="").strip()
        
        self.student.update_student(
            student_id=student_id,
            name=name if name else None,
            age=age,
            course=course if course else None,
            email=email if email else None
        )
    
    def handle_view_all_students(self):
        console.print(Panel.fit("[bold cyan]VIEW ALL STUDENTS[/bold cyan]", border_style="cyan"))
        self.student.view_all_students()
    
    def cleanup(self):
        self.db.disconnect()


def main():
    system = StudentRegistrationSystem()
    
    try:
        system.run()
    except KeyboardInterrupt:
        console.print("\n\n[green]✓ Interrupted by user[/green]")
    except Exception as e:
        console.print(f"\n[red]✗ An error occurred: {e}[/red]")
    finally:
        system.cleanup()
        console.print("\n[green]✓ Finished. Goodbye![/green]")


if __name__ == "__main__":
    main()
