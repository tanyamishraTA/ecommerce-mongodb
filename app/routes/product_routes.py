from fastapi import APIRouter
from app.schemas.product_schema import ProductCreate
from app.services.product_service import (
    add_product,
    fetch_products
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create(product: ProductCreate):
    product_id = add_product(product)

    return {
        "message": "Product created successfully",
        "product_id": product_id
    }


@router.get("/")
def get_all():
    return fetch_products()