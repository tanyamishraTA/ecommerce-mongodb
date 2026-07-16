from bson import ObjectId
from app.database.connection import db

products = db["products"]


def create_product(data):
    data["category_id"] = ObjectId(data["category_id"])
    result = products.insert_one(data)
    return str(result.inserted_id)


def get_products():
    return list(products.find())