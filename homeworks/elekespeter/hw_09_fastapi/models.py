from uuid import uuid1

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Product(Base):
    """A webshop egy terméke - ez lesz a "products" tábla az adatbázisban."""

    __tablename__ = "products"

    # Primary key: egyedi azonosító, amit az adatbázis-réteg generál uuid1()-gyel,
    # így a felhasználónak nem kell megadnia.
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)    # pl. morzsaporszívó
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)    # pl. 12 (darab)
    price: Mapped[int] = mapped_column(Integer, nullable=False)       # pl. 24900 (Ft, egész szám)
    category: Mapped[str | None] = mapped_column(String, nullable=True)  # opcionális
