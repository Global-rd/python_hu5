from pydantic import BaseModel, ConfigDict, Field


class ProductRequest(BaseModel):
    """
    Amit a kliens küld (létrehozás és frissítés). Nincs benne id,
    mert azt a szerver generálja.
    A Field() szabályai miatt hibás adatra a FastAPI magától 422-es hibát ad.
    """

    item_name: str = Field(..., min_length=1, examples=["morzsaporszívó"])
    quantity: int = Field(..., ge=0, examples=[12])          # nem lehet negatív
    price: int = Field(..., ge=0, examples=[24900])          # nem lehet negatív
    category: str | None = Field(default=None, examples=["háztartási gép"])  # opcionális


class ProductResponse(ProductRequest):
    """Amit a szerver visszaad: ugyanazok a mezők + a generált id."""

    # Engedi, hogy a SQLAlchemy Product objektumból közvetlenül válasz készüljön
    model_config = ConfigDict(from_attributes=True)

    id: str
