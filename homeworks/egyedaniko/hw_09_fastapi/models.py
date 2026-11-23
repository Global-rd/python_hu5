from uuid import uuid4

from sqlalchemy import CheckConstraint, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Product(Base):
    __tablename__ = "products"

    # Az adatbázis szintjén is tiltjuk a negatív mennyiséget és árat.
    __table_args__ = (
        CheckConstraint("quantity >= 0", name="quantity_non_negative"),
        CheckConstraint("price >= 0", name="price_non_negative"),
    )

    # A default egy függvény: minden új termék külön UUID-t kap.
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )
    item_name: Mapped[str] = mapped_column(String(200), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    # A kategória elhagyható, ilyenkor NULL kerül az adatbázisba.
    category: Mapped[str | None] = mapped_column(
        String(100), nullable=True, default=None
    )
