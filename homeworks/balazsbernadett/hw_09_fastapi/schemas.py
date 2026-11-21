from pydantic import BaseModel, Field


class ItemRequest(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: int = Field(..., ge=0)
    category: str | None = None


class ItemResponse(ItemRequest):
    id: str