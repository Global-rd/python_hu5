from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.products import (
    create_product,
    delete_product_by_id,
    get_all_products,
    get_product_by_id,
    update_product_by_id,
)
from models import Product
from schemas import ProductRequest

async def list_products_service(db: AsyncSession) -> list[Product]:
    """Lekeri az osszes termeket az adatbazis-retegen keresztul."""
    return await get_all_products(db)

async def get_product_service(product_id: str, db: AsyncSession) -> Product:
    """Lekeri a termeket, vagy 404-es hibat ad, ha nem talalhato."""
    product = await get_product_by_id(product_id, db)
    if product is None:
        raise HTTPException(status_code=404, detail="A termek nem talalhato")
    return product

async def create_product_service(product: ProductRequest, db: AsyncSession) -> Product:
    """Tovabbitja az uj termek letrehozasat az adatbazis-retegnek."""
    return await create_product(product, db)

async def update_product_service(product_id: str, product_update: ProductRequest, db: AsyncSession) -> Product:
    """Megkeresi, majd frissiti a termeket."""
    product = await get_product_service(product_id, db)
    return await update_product_by_id(product, product_update, db)

async def delete_product_service(product_id: str, db: AsyncSession) -> None:
    """Megkeresi, majd torli a termeket."""
    product = await get_product_service(product_id, db)
    await delete_product_by_id(product, db)
