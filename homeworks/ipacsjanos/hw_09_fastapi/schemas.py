from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None

class ItemResponse(ItemBase):
    id: str

    class Config:
        from_attributes = True
