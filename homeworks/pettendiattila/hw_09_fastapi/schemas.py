
from pydantic import BaseModel, Field
from typing import Optional


class ProductRequest(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)
    category: Optional[str] = None


class ProductResponse(ProductRequest):
    id: str
