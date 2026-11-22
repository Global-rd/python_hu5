# küldök egy requestet az endpointra
# az meghívja a servicet
# a service meghívja az adatbázis műveletet

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.products import (
    get_all_products,
    get_product_by_id,
    insert_product,
    delete_product_by_id,
    update_product_by_id
)

from models import Product
from schemas import ProductRequest

async def list_products_service(db: AsyncSession) -> list[Product]:
    return await get_all_products(db)

async def insert_product_service(product:ProductRequest, db: AsyncSession) -> Product:
    return await insert_product(product, db)

async def get_product_service(product_id: str, db: AsyncSession) -> Product:
    product = await get_product_by_id(product_id, db)

    if product is None:
        raise HTTPException(status_code=404, detail=f"Product id {product_id} is not found ")
    
    return product

async def update_product_service(product_id: str , product_update: ProductRequest, db: AsyncSession) -> Product:
    product = await get_product_service(product_id, db)
    return await update_product_by_id(product, product_update, db)

async def delete_product_service(product_id: str, db: AsyncSession) -> Product:
    product = await get_product_service(product_id, db)
    return await delete_product_by_id(product, db)