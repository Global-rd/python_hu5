from uuid import uuid1
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, column_property, relationship
from datetime import datetime
from webshop_db import Base

class Stock(Base):

    __tablename__ = "items"

    item_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True, default='')


class Customer(Base):

    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    customer_name: Mapped[str] = mapped_column(String, nullable=False)
    customer_email: Mapped[str] = mapped_column(String, nullable=False)


class Order(Base):

    __tablename__ = "orders"

    order_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    order_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    customer_id: Mapped[str] = mapped_column(String, ForeignKey("customers.customer_id"), nullable=False)
    item_id: Mapped[str] = mapped_column(String, ForeignKey("items.item_id"), nullable=False)
    item_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    order_value: Mapped[float] = mapped_column(Float, nullable=False)
    customer: Mapped["Customer"] = relationship()
