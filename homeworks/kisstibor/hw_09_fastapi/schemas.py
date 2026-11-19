from pydantic import BaseModel, ConfigDict, Field

class ProductRequest(BaseModel):
    """Ellenorzi a termek letrehozasakor vagy frissitesekor kapott adatokat."""

    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: int = Field(..., ge=0)
    category: str | None = None

class ProductResponse(ProductRequest):
    """A termek API-valaszban visszaadott adatait irja le."""

    model_config = ConfigDict(from_attributes=True)

    id: str
