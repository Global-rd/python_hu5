from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid1

app = FastAPI(
    title="Webshop Product API",
    description="Egyszerű CRUD API termékek kezelésére",
    version="1.0.0"
)

# ===== MODELS =====

class ProductCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class ProductUpdate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


class Product(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None


# ===== IN-MEMORY DATABASE =====

products: dict[str, Product] = {}


# ===== CREATE =====

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    product_id = str(uuid1())

    new_product = Product(
        id=product_id,
        item_name=product.item_name,
        quantity=product.quantity,
        price=product.price,
        category=product.category
    )

    products[product_id] = new_product

    return new_product


# ===== READ ALL =====

@app.get("/products", response_model=list[Product])
def get_products():
    return list(products.values())


# ===== READ ONE =====

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = products.get(product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# ===== UPDATE =====

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, updated_product: ProductUpdate):
    existing_product = products.get(product_id)

    if not existing_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product = Product(
        id=product_id,
        item_name=updated_product.item_name,
        quantity=updated_product.quantity,
        price=updated_product.price,
        category=updated_product.category
    )

    products[product_id] = product

    return product


# ===== DELETE =====

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted successfully",
        "deleted_product": deleted_product
    }
