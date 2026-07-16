from app.database.connection import db
from datetime import datetime

users = db["users"]


def create_user(user_data):
    user_data["created_at"] = datetime.utcnow()

    result = users.insert_one(user_data)

    return str(result.inserted_id)


def get_users():
    return list(users.find())