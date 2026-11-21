

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ItemBase(BaseModel):
    """Shared properties for an item."""

    item_name: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., gt=0)
    category: Optional[str] = Field(None, max_length=50)


class ItemCreate(ItemBase):
    """Properties required to create a new item (excludes ID)."""

    pass


class ItemUpdate(BaseModel):
    """Properties allowed when updating an existing item."""

    item_name: Optional[str] = Field(None, min_length=1, max_length=100)
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, max_length=50)


class ItemResponse(ItemBase):
    """Properties returned to the client (includes generated ID)."""

    id: str

    model_config = ConfigDict(from_attributes=True)

    