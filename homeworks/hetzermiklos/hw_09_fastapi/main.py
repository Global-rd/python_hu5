
from uuid import uuid1
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Webshop terméknyilvántartó")


# Termék adatmodellje
class ProductCreate(BaseModel):
    item_name: str
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    category: Optional[str] = None


class Product(ProductCreate):
    id: str


# Egyszerű, memóriában tárolt terméknyilvántartás
products = {}


# Összes termék lekérdezése
@app.get("/products", response_model=list[Product])
def get_products():
    return list(products.values())


# Egy termék lekérdezése azonosító alapján
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Termék nem található")

    return products[product_id]


# Új termék létrehozása
@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    product_id = str(uuid1())

    new_product = Product(
        id=product_id,
        **product.model_dump()
    )

    products[product_id] = new_product
    return new_product


# Termék adatainak módosítása
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, product: ProductCreate):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Termék nem található")

    updated_product = Product(
        id=product_id,
        **product.model_dump()
    )

    products[product_id] = updated_product
    return updated_product


# Termék törlése
@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Termék nem található")

    del products[product_id]
    return {"message": "Termék sikeresen törölve"}
