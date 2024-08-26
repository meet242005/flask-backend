from datetime import datetime
from uuid import uuid4
from models.auth_models import User
from settings.db import db

def get_user_by_email(email):
    user_data = db.users.find_one({"email": email})
    if user_data:
        return User(email=user_data['email'], hashed_password=user_data['hashed_password'], date_created=user_data['date_created'], uid=user_data['uid'])
    return None

def create_user(email, password):
    user = User(email, password, date_created=datetime.now(), uid=str(uuid4()))
    db.users.insert_one(user.to_dict())
    return user
