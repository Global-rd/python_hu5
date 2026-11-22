from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
from contextlib import closing
from pathlib import Path
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Az new vagy modified termék adatai
class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: str | None = None

# Az összes termék listázása:
@app.get("/items")
def list_items():
    db_path = Path(__file__).with_name("inventory.db")


    with closing(sqlite3.connect(db_path)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute("SELECT * FROM items").fetchall()
        return [dict(row) for row in rows]

# Új termék mentése / létrehozása
@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        cursor = connection.execute(
            """
            INSERT INTO items (item_name, quantity, price, category)
            VALUES (?, ?, ?, ?)
            """,
            (item.item_name, item.quantity, item.price, item.category),
        )
        item_id = cursor.lastrowid  # Az új termék ID alapján történő kiolvasása
        connection.commit()

    return {"id": item_id, **item.model_dump()}

# Egy termék lekérése ID alapján
@app.get("/items/{item_id}")
def get_item(item_id: str):
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        connection.row_factory = sqlite3.Row

        row = connection.execute(
            "SELECT * FROM items WHERE id = ?", (item_id,)
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Item hasn't been found")

    return dict(row)


# Egy Item módosítása
@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        cursor = connection.execute(
            """
            UPDATE items
            SET item_name = ?, quantity = ?, price = ?, category = ?
            WHERE id = ?
            """,
            (item.item_name, item.quantity, item.price, item.category, item_id),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item hasn't been found")

        connection.commit()

    return {"id": item_id, **item.model_dump()}


#Egy elem / item törlése ID alapján
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db_path = Path(__file__).with_name("inventory.db")

    with closing(sqlite3.connect(db_path)) as connection:
        cursor = connection.execute(
            "DELETE FROM items WHERE id = ?", (item_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item hasn't been found")

        connection.commit()

    return {"message": "Item deleted", "id": item_id}






