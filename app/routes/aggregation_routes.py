from fastapi import APIRouter

from app.services.aggregation_service import (
    fetch_user_orders,
    fetch_product_categories,
    fetch_user_purchase_summary
)

router = APIRouter(
    prefix="/aggregation",
    tags=["Aggregation"]
)


# Query 1
@router.get("/user-orders")
def user_orders():
    return fetch_user_orders()


# Query 2
@router.get("/product-category")
def product_category():
    return fetch_product_categories()


# Query 3
@router.get("/user-purchase-summary")
def user_purchase_summary():
    return fetch_user_purchase_summary()