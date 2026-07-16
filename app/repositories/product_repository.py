from bson import ObjectId

from app.database.connection import db
from app.utils.serializer import serialize_data

products = db["products"]


def create_product(data):
    data["category_id"] = ObjectId(data["category_id"])

    result = products.insert_one(data)

    return str(result.inserted_id)


def get_products():
    product_list = list(products.find())
    return serialize_data(product_list)