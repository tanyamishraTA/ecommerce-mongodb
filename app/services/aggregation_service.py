from app.repositories.aggregation_repository import (
    get_user_orders,
    get_product_categories,
    get_user_purchase_summary
)


def fetch_user_orders():
    return get_user_orders()


def fetch_product_categories():
    return get_product_categories()


def fetch_user_purchase_summary():
    return get_user_purchase_summary()