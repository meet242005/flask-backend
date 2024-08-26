from passlib.hash import bcrypt

class User:
    def __init__(self, email, password=None, hashed_password=None, date_created=None, uid=None):
        self.email = email
        self.hashed_password = hashed_password or bcrypt.hash(password)
        self.date_created = date_created
        self.uid = uid

    def verify_password(self, password):
        return bcrypt.verify(password, self.hashed_password)

    def to_dict(self):
        return {
            "email": self.email,
            "hashed_password": self.hashed_password,
            "date_created": self.date_created,
            "uid": self.uid
        }
