from contextlib import asynccontextmanager
from uuid import uuid1

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, String, Integer, Float
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
    sessionmaker,
)


DATABASE_URL = "sqlite:///./webshop.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid1())
    )

    item_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )


class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: str | None = None


class ItemUpdate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: str | None = None


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    item_name: str
    quantity: int
    price: float
    category: str | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Webshop Product API",
    description="A simple webshop product management API",
    version="1.0.0",
    lifespan=lifespan
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Webshop Product API is running."
    }


@app.get(
    "/items",
    response_model=list[ItemResponse]
)
def get_all_items(
    db: Session = Depends(get_db)
):
    items = db.query(Item).all()

    return items


@app.get(
    "/items/{item_id}",
    response_model=ItemResponse
)
def get_item(
    item_id: str,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found."
        )

    return item


@app.post(
    "/items",
    response_model=ItemResponse,
    status_code=201
)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db)
):
    new_item = Item(
        item_name=item_data.item_name,
        quantity=item_data.quantity,
        price=item_data.price,
        category=item_data.category
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@app.put(
    "/items/{item_id}",
    response_model=ItemResponse
)
def update_item(
    item_id: str,
    item_data: ItemUpdate,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found."
        )

    item.item_name = item_data.item_name
    item.quantity = item_data.quantity
    item.price = item_data.price
    item.category = item_data.category

    db.commit()
    db.refresh(item)

    return item


@app.delete(
    "/items/{item_id}"
)
def delete_item(
    item_id: str,
    db: Session = Depends(get_db)
):
    item = db.query(Item).filter(
        Item.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found."
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Item successfully deleted.",
        "id": item_id
    }