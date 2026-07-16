from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    city: str


class UserResponse(UserCreate):
    id: str
    created_at: datetime