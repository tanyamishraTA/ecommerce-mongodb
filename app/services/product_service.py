from app.repositories.product_repository import (
    create_product,
    get_products
)


def add_product(product):
    return create_product(product.model_dump())


def fetch_products():
    return get_products()