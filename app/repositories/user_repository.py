from datetime import datetime

from app.database.connection import db
from app.utils.serializer import serialize_data

users = db["users"]


def create_user(user_data):
    user_data["created_at"] = datetime.utcnow()

    result = users.insert_one(user_data)

    return str(result.inserted_id)


def get_users():
    users_list = list(users.find())
    return serialize_data(users_list)