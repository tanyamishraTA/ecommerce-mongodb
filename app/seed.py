from datetime import datetime
from app.database.connection import db

# Collections
users_collection = db["users"]
categories_collection = db["categories"]
products_collection = db["products"]
orders_collection = db["orders"]


def seed_database():
    # Clear existing data
    users_collection.delete_many({})
    categories_collection.delete_many({})
    products_collection.delete_many({})
    orders_collection.delete_many({})

    print("Existing data deleted.")

    # -------------------------
    # Categories
    # -------------------------
    categories = [
        {
            "name": "Electronics",
            "description": "Electronic gadgets"
        },
        {
            "name": "Fashion",
            "description": "Clothing and accessories"
        },
        {
            "name": "Books",
            "description": "Books and stationery"
        }
    ]

    category_result = categories_collection.insert_many(categories)

    electronics_id = category_result.inserted_ids[0]
    fashion_id = category_result.inserted_ids[1]
    books_id = category_result.inserted_ids[2]

    print("Categories inserted.")

    # -------------------------
    # Products
    # -------------------------
    products = [
        {
            "name": "MacBook Air M2",
            "brand": "Apple",
            "price": 95000,
            "stock": 15,
            "category_id": electronics_id
        },
        {
            "name": "Nike Shoes",
            "brand": "Nike",
            "price": 6000,
            "stock": 30,
            "category_id": fashion_id
        },
        {
            "name": "Atomic Habits",
            "brand": "Penguin",
            "price": 550,
            "stock": 100,
            "category_id": books_id
        }
    ]

    product_result = products_collection.insert_many(products)

    macbook_id = product_result.inserted_ids[0]
    shoes_id = product_result.inserted_ids[1]
    book_id = product_result.inserted_ids[2]

    print("Products inserted.")

    # -------------------------
    # Users
    # -------------------------
    users = [
        {
            "name": "Tanya Mishra",
            "email": "tanya@gmail.com",
            "phone": "9876543210",
            "city": "Noida",
            "created_at": datetime.now()
        },
        {
            "name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "phone": "9876543211",
            "city": "Delhi",
            "created_at": datetime.now()
        },
        {
            "name": "Anjali Verma",
            "email": "anjali@gmail.com",
            "phone": "9876543212",
            "city": "Lucknow",
            "created_at": datetime.now()
        }
    ]

    user_result = users_collection.insert_many(users)

    tanya_id = user_result.inserted_ids[0]
    rahul_id = user_result.inserted_ids[1]
    anjali_id = user_result.inserted_ids[2]

    print("Users inserted.")

    # -------------------------
    # Orders
    # -------------------------
    orders = [
        {
            "user_id": tanya_id,
            "product_id": macbook_id,
            "quantity": 1,
            "total_amount": 95000,
            "status": "Delivered",
            "order_date": datetime.now()
        },
        {
            "user_id": tanya_id,
            "product_id": book_id,
            "quantity": 2,
            "total_amount": 1100,
            "status": "Delivered",
            "order_date": datetime.now()
        },
        {
            "user_id": rahul_id,
            "product_id": shoes_id,
            "quantity": 1,
            "total_amount": 6000,
            "status": "Processing",
            "order_date": datetime.now()
        },
        {
            "user_id": anjali_id,
            "product_id": book_id,
            "quantity": 3,
            "total_amount": 1650,
            "status": "Delivered",
            "order_date": datetime.now()
        }
    ]

    orders_collection.insert_many(orders)

    print("Orders inserted.")
    print("\nDatabase seeded successfully!")


if __name__ == "__main__":
    seed_database()