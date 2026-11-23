

import uuid
from sqlalchemy import Column, Float, Integer, String
from database import Base


def generate_uuid() -> str:
    """Generate a UUID1 string."""
    return str(uuid.uuid1())


class Item(Base):
    """Database model representing a webshop item."""

    __tablename__ = "items"

    id = Column(
        String(36),
        primary_key=True,
        default=generate_uuid,
        index=True,
    )
    item_name = Column(String(100), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=0)
    price = Column(Float, nullable=False)
    category = Column(String(50), nullable=True)

    