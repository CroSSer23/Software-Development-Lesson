import hashlib
from rich.console import Console

console = Console()


class User:
    
    def __init__(self, db):
        self.db = db
        self.current_user = None
    
    def register(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        
        check_query = "SELECT * FROM users WHERE username = %s"
        existing_user = self.db.fetch_query(check_query, (username,))
        
        if existing_user:
            console.print(f"\n[red]✗ Username '{username}' already exists![/red]")
            return False
        
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        
        if self.db.execute_query(insert_query, (username, hashed)):
            console.print(f"\n[green]✓ User '{username}' registered successfully![/green]")
            return True
        else:
            console.print("\n[red]✗ Registration failed![/red]")
            return False
    
    def login(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        result = self.db.fetch_query(query, (username, hashed))
        
        if result and len(result) > 0:
            self.current_user = result[0]
            console.print(f"\n[green]✓ Welcome, {username}![/green]")
            return True
        else:
            console.print("\n[red]✗ Invalid username or password![/red]")
            return False
    
    def logout(self):
        if self.current_user:
            username = self.current_user['username']
            self.current_user = None
            console.print(f"\n[green]✓ User '{username}' logged out successfully![/green]")
            return True
        return False
    
    def is_logged_in(self):
        return self.current_user is not None
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def get_current_user(self):
        return self.current_user
