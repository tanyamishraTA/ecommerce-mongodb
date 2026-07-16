from fastapi import APIRouter
from app.schemas.order_schema import OrderCreate
from app.services.order_service import (
    add_order,
    fetch_orders
)

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def create(order: OrderCreate):
    order_id = add_order(order)

    return {
        "message": "Order created successfully",
        "order_id": order_id
    }


@router.get("/")
def get_all():
    return fetch_orders()