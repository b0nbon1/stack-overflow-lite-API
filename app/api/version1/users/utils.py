import re
from app.api.version1.users.models import User, Users

class validators(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)

    def validate_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False
        if not len(self.email) >= 12:
            return False
        else:
            return True

    def validate_password(self):
        if not len(self.password) >= 6 and len(self.password) <= 16:
            return False

    def validate_username(self):
        if not len(self.username) >= 3:
            return False

    def username_exists(self):
        user = [user for user in Users if user['username'] == self.username]
        if user:
            return True
        else:
            return False
