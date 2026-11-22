from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
from contextlib import closing
from pathlib import Path

app = FastAPI()

class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: str | None = None

@app.get("/items")
def list_items():
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute("SELECT * FROM items").fetchall()
        return [dict(row) for row in rows]


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):

    item_id = str(uuid4())
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        connection.execute(

            """
            INSERT INTO items (id, item_name, quantity, price, category)
            VALUES (?, ?, ?, ?, ?)
            """,


            (item_id, item.item_name, item.quantity, item.price, item.category),
        )
        connection.commit()

    return {"id": item_id, **item.model_dump()}