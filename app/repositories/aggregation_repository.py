from app.database.connection import db
from app.utils.serializer import serialize_data

users = db["users"]
products = db["products"]


# Query 1: User Order History
def get_user_orders():
    pipeline = [
    {
        "$lookup": {
            "from": "orders",
            "localField": "_id",
            "foreignField": "user_id",
            "as": "orders"
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "email": 1,
            "city": 1,
            "orders": {
                "$map": {
                    "input": "$orders",
                    "as": "order",
                    "in": {
                        "quantity": "$$order.quantity",
                        "total_amount": "$$order.total_amount",
                        "status": "$$order.status"
                    }
                }
            }
        }
    }
]

    result = list(users.aggregate(pipeline))
    return serialize_data(result)


# Query 2: Product with Category
def get_product_categories():
    pipeline = [
        {
            "$lookup": {
                "from": "categories",
                "localField": "category_id",
                "foreignField": "_id",
                "as": "category"
            }
        },
        {
            "$unwind": "$category"
        },
        {
            "$project": {
                "_id": 0,
                "product_name": "$name",
                "brand": 1,
                "price": 1,
                "stock": 1,
                "category_name": "$category.name",
                "category_description": "$category.description"
            }
        }
    ]

    result = list(products.aggregate(pipeline))
    return serialize_data(result)


# Query 3: User Purchase Summary
def get_user_purchase_summary():
    pipeline = [
        {
            "$lookup": {
                "from": "orders",
                "localField": "_id",
                "foreignField": "user_id",
                "as": "orders"
            }
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "email": 1,
                "total_orders": {
                    "$size": "$orders"
                },
                "total_spent": {
                    "$sum": "$orders.total_amount"
                }
            }
        }
    ]

    result = list(users.aggregate(pipeline))
    return serialize_data(result)