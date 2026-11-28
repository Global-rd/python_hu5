from uuid import uuid1
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from webshop_db import Base

class Product(Base):

    __tablename__ = "products"

    product_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    product_name: Mapped[str] = mapped_column(String, nullable=False)
    manufacturer: Mapped[str] = mapped_column(String, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True, default='')
    stock = relationship(
        "Stock",
        back_populates="product",
        uselist=False)

    
class Stock(Base):

    __tablename__ = "stock"

    stock_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    product_id: Mapped[str] = mapped_column(String, ForeignKey("products.product_id"))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    product = relationship(
        "Product",
        back_populates="stock")
    


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
    customer = relationship("Customer")
    items = relationship(
        "OrderLineItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    @property
    def order_value(self) -> float:
        return sum(item.order_value for item in self.items)


class OrderLineItem(Base):

    __tablename__ = "order_line_items"

    itemline_id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    order_id: Mapped[str] = mapped_column(String, ForeignKey("orders.order_id"), nullable=False)
    product_id: Mapped[str] = mapped_column(String, ForeignKey("products.product_id"), nullable=False)
    item_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    order_value: Mapped[float] = mapped_column(Float, nullable=False)
    unit_price: Mapped[float] = mapped_column(Float, nullable=False)
    order = relationship(
        "Order",
        back_populates="items")
    product = relationship("Product")



