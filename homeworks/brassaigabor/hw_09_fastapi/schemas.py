from pydantic import BaseModel, Field, ConfigDict

#pydantic model

class ItemRequest(BaseModel): # kliens -> szerver

    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: int = Field(..., ge=0)
    category: str | None = None

class ItemResponse(ItemRequest): # szerver -> kliens

    model_config = ConfigDict(from_attributes=True)

    id: str
