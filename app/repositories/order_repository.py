from bson import ObjectId

from app.database.connection import db
from app.utils.serializer import serialize_data

orders = db["orders"]


def create_order(data):
    data["user_id"] = ObjectId(data["user_id"])
    data["product_id"] = ObjectId(data["product_id"])

    result = orders.insert_one(data)

    return str(result.inserted_id)


def get_orders():
    order_list = list(orders.find())
    return serialize_data(order_list)