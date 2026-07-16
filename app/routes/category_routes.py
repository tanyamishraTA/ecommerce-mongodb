from fastapi import APIRouter
from app.schemas.category_schema import CategoryCreate
from app.services.category_service import (
    add_category,
    fetch_categories
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create(category: CategoryCreate):
    category_id = add_category(category)
    return {"category_id": category_id}


@router.get("/")
def get_all():
    return fetch_categories()