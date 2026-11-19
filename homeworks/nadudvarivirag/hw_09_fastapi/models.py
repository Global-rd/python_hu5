from uuid import uuid1
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Product(Base):
    __tablename__ = "products"  #itt adom meg a konkrét tábla nevet

    # Itt adom meg hogy milyen oszlopnevek legyenek
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1())) 
     #(egyedi azonosító, pl uuid1 által generált) a lambdával késleltetjük a UUID generálását addig, amíg az SQLAlchemy-nek ténylegesen szüksége nem lesz rá.
    product_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True, default="")



