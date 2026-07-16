from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: str
    product_id: str
    quantity: int
    total_amount: float
    status: str