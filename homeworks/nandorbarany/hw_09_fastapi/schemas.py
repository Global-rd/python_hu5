from pydantic import BaseModel


class ProductRequest(BaseModel):

    item_name: str
    quantity: int
    price: int

    category: str | None = None


class ProductResponse(ProductRequest):

    id: str
