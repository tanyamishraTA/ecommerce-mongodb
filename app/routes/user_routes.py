from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import (
    add_user,
    fetch_users
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create(user: UserCreate):
    user_id = add_user(user)

    return {
        "message": "User created successfully",
        "user_id": user_id
    }


@router.get("/")
def get_all():
    return fetch_users()