from app.repositories.user_repository import (
    create_user,
    get_users
)


def add_user(user):
    return create_user(user.model_dump())


def fetch_users():
    return get_users()