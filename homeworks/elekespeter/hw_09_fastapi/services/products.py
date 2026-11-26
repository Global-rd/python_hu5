from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud.products import (
    create_product,
    delete_product,
    get_all_products,
    get_product_by_id,
    update_product,
)
from models import Product
from schemas import ProductRequest

# A service réteg az "üzleti logika": itt dől el például, hogy mi számít hibának.


async def list_products_service(db: AsyncSession) -> list[Product]:
    return await get_all_products(db)


async def create_product_service(product: ProductRequest, db: AsyncSession) -> Product:
    return await create_product(product, db)


async def get_product_service(product_id: str, db: AsyncSession) -> Product:
    """Visszaadja a terméket, vagy 404-es hibát dob, ha nincs ilyen id."""
    product = await get_product_by_id(product_id, db)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product id {product_id} not found",
        )
    return product


async def update_product_service(product_id: str, product_update: ProductRequest,
                                 db: AsyncSession) -> Product:
    # Előbb megkeressük (ha nincs, a get_product_service már 404-et dob)
    product = await get_product_service(product_id, db)
    return await update_product(product, product_update, db)


async def delete_product_service(product_id: str, db: AsyncSession) -> Product:
    product = await get_product_service(product_id, db)
    return await delete_product(product, db)
