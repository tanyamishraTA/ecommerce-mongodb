from app.repositories.category_repository import (
    create_category,
    get_categories
)


def add_category(category):
    return create_category(category.model_dump())


def fetch_categories():
    return get_categories()