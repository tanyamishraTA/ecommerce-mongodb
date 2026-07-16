from app.database.connection import db
from app.utils.serializer import serialize_data

categories = db["categories"]


def create_category(data):
    result = categories.insert_one(data)
    return str(result.inserted_id)


def get_categories():
    category_list = list(categories.find())
    return serialize_data(category_list)