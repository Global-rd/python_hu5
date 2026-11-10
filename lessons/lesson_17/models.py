from uuid import uuid1
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Movie(Base):

    __tablename__ = "movies"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    title: Mapped[str] = mapped_column(String, nullable=False)
    genre: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    length_in_mins: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False, default=0)






