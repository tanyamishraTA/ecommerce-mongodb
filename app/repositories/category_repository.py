from app.database.connection import db

categories = db["categories"]


def create_category(data):
    result = categories.insert_one(data)
    return str(result.inserted_id)


def get_categories():
    return list(categories.find())