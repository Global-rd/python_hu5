from pydantic import BaseModel, ConfigDict, Field


# Létrehozás és teljes frissítés során fogadott adatok.
class ProductCreate(BaseModel):
    # Levágjuk a szélső szóközöket, és tiltjuk az ismeretlen mezőket (pl. id).
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    item_name: str = Field(min_length=1, max_length=200)
    quantity: int = Field(ge=0, le=2_147_483_647, strict=True)
    price: float = Field(ge=0, allow_inf_nan=False, strict=True)
    category: str | None = Field(default=None, min_length=1, max_length=100)


# A válasz már tartalmazza a generált azonosítót is.
class ProductResponse(ProductCreate):
    # SQLAlchemy objektum attribútumaiból is előállítható a válasz.
    model_config = ConfigDict(from_attributes=True)

    id: str
