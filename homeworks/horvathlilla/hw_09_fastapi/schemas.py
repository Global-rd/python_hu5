from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    item_name: str = Field(..., example="morzsaporszívó")
    quantity: int = Field(..., example=12)
    price: float = Field(..., example=2490.0)
    category: str = Field(None, example="háztartási gép")

class ProductResponse(ProductRequest):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    