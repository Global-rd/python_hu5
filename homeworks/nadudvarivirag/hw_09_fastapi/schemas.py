from pydantic import BaseModel, Field #adatvalidáció

# eltér a kért és a vissza adott adat

class ProductRequest(BaseModel):

    product_name: str = Field(..., min_length = 1)
    quantity: int
    price: int

    category: str = ""

class ProductResponse(ProductRequest):
    
    id: str