import hashlib


class User:
    
    def __init__(self, database):
        self.database = database
        self.current_user = None
    
    def register(self, username, password, email):
        pass
    
    def login(self, username, password):
        pass
    
    def logout(self):
        pass
    
    def is_logged_in(self):
        return self.current_user is not None
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def get_current_user(self):
        return self.current_user

