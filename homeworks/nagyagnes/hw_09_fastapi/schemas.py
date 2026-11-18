
from pydantic import BaseModel, Field


class ProductRequest(BaseModel):

    item_name: str = Field(..., min_length=1)
    quantity: int
    price: int
    category: str | None = None


class ProductResponse(ProductRequest):

    id: str
