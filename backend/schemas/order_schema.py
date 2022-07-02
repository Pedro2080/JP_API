from typing import Optional

from datetime import datetime
from pydantic import BaseModel, constr


class OrderCreate(BaseModel):
    user_id: Optional[int]
    product_id: Optional[int]
    quantity: int
    delivery_address: constr(max_length=120)
    comments: Optional[constr(max_length=120)] = "No comments"

    time_created: datetime = datetime.now()
    time_updated: datetime = datetime.now()


class OrderDTO(BaseModel):
    id: Optional[int] = None
    quantity: int
    delivery_address: constr(max_length=120)
    comments: Optional[constr(max_length=120)] = "No comments"

    class Config:
        orm_mode = True