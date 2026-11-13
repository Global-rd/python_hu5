from pydantic import BaseModel, Field

class WebshopRequest(BaseModel):

    item_name: str = Field(..., min_length=1)
    quantity: int
    price: int

    category: str | None = None

class WebshopResponse(WebshopRequest):

    id: str