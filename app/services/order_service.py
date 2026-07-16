from app.repositories.order_repository import (
    create_order,
    get_orders
)


def add_order(order):
    return create_order(order.model_dump())


def fetch_orders():
    return get_orders()