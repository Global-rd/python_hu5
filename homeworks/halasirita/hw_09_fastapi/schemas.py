
from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    item_name: str = Field(min_length=1)
    quantity: int = Field(ge=0)
    price: int = Field(ge=0)
    category: str | None = None


class ProductResponse(ProductCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)
