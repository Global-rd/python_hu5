"""A small SQLite-backed product registry with five CRUD endpoints."""

from contextlib import asynccontextmanager, closing
from pathlib import Path
import sqlite3
from typing import Annotated
from uuid import UUID, uuid4

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field, StringConstraints


DATABASE = Path(__file__).with_name("webshop.db")
ProductName = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class ProductCreate(BaseModel):
    """Fields supplied by a client when creating or replacing a product."""

    item_name: ProductName
    quantity: int = Field(ge=0)
    price: int = Field(ge=0, description="Price in whole currency units")
    category: str | None = None


class Product(ProductCreate):
    """The public product representation includes its generated identifier."""

    id: UUID


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Create the products table when the application starts."""

    with closing(sqlite3.connect(DATABASE)) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                price INTEGER NOT NULL CHECK (price >= 0),
                category TEXT
            )
            """
        )
        connection.commit()
    yield


app = FastAPI(title="Webshop Product Registry", lifespan=lifespan)


def get_connection():
    """Give each request its own SQLite connection and close it afterwards."""

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


DbConnection = Annotated[sqlite3.Connection, Depends(get_connection)]


@app.get("/products", response_model=list[Product])
def list_products(connection: DbConnection) -> list[Product]:
    """List every product."""

    rows = connection.execute("SELECT * FROM products ORDER BY item_name, id").fetchall()
    return [Product(**dict(row)) for row in rows]


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: UUID, connection: DbConnection) -> Product:
    """Return one product or an HTTP 404 response."""

    row = connection.execute(
        "SELECT * FROM products WHERE id = ?", (str(product_id),)
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return Product(**dict(row))


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, connection: DbConnection) -> Product:
    """Generate an ID on the server and save a new product."""

    product_id = uuid4()
    connection.execute(
        "INSERT INTO products (id, item_name, quantity, price, category) "
        "VALUES (?, ?, ?, ?, ?)",
        (str(product_id), product.item_name, product.quantity,
         product.price, product.category),
    )
    connection.commit()
    return Product(id=product_id, **product.model_dump())


@app.put("/products/{product_id}", response_model=Product)
def update_product(
    product_id: UUID, product: ProductCreate, connection: DbConnection
) -> Product:
    """Replace the editable fields of an existing product."""

    if connection.execute(
        "SELECT 1 FROM products WHERE id = ?", (str(product_id),)
    ).fetchone() is None:
        raise HTTPException(status_code=404, detail="Product not found")

    connection.execute(
        "UPDATE products SET item_name = ?, quantity = ?, price = ?, "
        "category = ? WHERE id = ?",
        (product.item_name, product.quantity, product.price,
         product.category, str(product_id)),
    )
    connection.commit()
    return Product(id=product_id, **product.model_dump())


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: UUID, connection: DbConnection) -> None:
    """Delete one product; report HTTP 404 when the ID is unknown."""

    result = connection.execute(
        "DELETE FROM products WHERE id = ?", (str(product_id),)
    )
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    connection.commit()
