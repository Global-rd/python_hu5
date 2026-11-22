
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Product
from schemas import ProductCreate, ProductResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="Webshop Product API",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {"message": "Webshop API is running!"}


@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=201
)
async def create_product(
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    new_product = Product(**product_data.model_dump())

    db.add(new_product)

    await db.commit()

    await db.refresh(new_product)

    return new_product

@app.get(
    "/products",
    response_model=list[ProductResponse]
)
async def get_products(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Product))

    products = result.scalars().all()

    return products


@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
async def get_product(
    product_id: str,
    db: AsyncSession = Depends(get_db)
):
    product = await db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@app.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
async def update_product(
    product_id: str,
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    product = await db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for field, value in product_data.model_dump().items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)

    return product


@app.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
async def update_product(
    product_id: str,
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    product = await db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for field, value in product_data.model_dump().items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)

    return product


@app.delete(
    "/products/{product_id}",
    status_code=204
)
async def delete_product(
    product_id: str,
    db: AsyncSession = Depends(get_db)
):
    product = await db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    await db.delete(product)
    await db.commit()
