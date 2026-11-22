
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    item_name: Mapped[str] = mapped_column(nullable=False)

    quantity: Mapped[int] = mapped_column(nullable=False)

    price: Mapped[int] = mapped_column(nullable=False)

    category: Mapped[str | None] = mapped_column(
        nullable=True,
        default=None
    )
