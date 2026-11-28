from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    price: int = Field(..., gt=0)
    category: str = Field(..., min_length=1)

class ProductResponse(ProductRequest):
    id: str
