from uuid import UUID, uuid4

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class ItemInput(SQLModel):
    """A hozzáadáskor és módosításkor beküldhető adatok."""

    # Levágja a szövegek elejéről és végéről a szóközöket.
    # Nem enged meg további, ismeretlen mezőket.
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    item_name: str = Field(min_length=1, max_length=150)
    quantity: int = Field(ge=0)
    price: int = Field(ge=0)

    # A kategória elhagyható.
    category: str | None = Field(default=None, max_length=100)


class Item(ItemInput, table=True):
    """Az adatbázisban tárolt termék."""

    __tablename__ = "items"

    # Minden új termék automatikusan új azonosítót kap.
    # A primary_key=True jelenti az elsődleges kulcsot.
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class ItemOutput(ItemInput):
    """A válaszban visszaadott adatok, az azonosítóval együtt."""

    id: UUID