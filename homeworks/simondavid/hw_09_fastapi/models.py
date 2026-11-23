from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    # Basic product information
    item_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)

    # Physical specifications
    scale = Column(String, nullable=True)
    height_cm = Column(Float, nullable=True)
    width_cm = Column(Float, nullable=True)
    depth_cm = Column(Float, nullable=True)
    material = Column(String, default="Resin", nullable=False)
    painted = Column(Boolean, default=False, nullable=False)

    # Pricing and availability
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    made_to_order = Column(Boolean, default=True, nullable=False)
    production_days = Column(Integer, default=7, nullable=False)

    # Product image and visibility
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)