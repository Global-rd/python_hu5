# adatbázisdefiníció

from uuid import uuid1
# ha több db is van, amiket összeszinkronizálunk, a sima autoincrement nem biztosít egyedi kulcsot
from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from decimal import Decimal

class Item(Base):

    __tablename__ = "items"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True)





