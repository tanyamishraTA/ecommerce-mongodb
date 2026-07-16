from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    brand: str
    price: float
    stock: int
    category_id: str