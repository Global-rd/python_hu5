from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from crud.webshop import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product_by_id,
    delete_product_by_id
)
from models import WebshopProducts
from schemas import WebshopRequest

async def list_products_sevice(db: AsyncSession) -> list[WebshopProducts]:
    return await get_all_products(db)

async def create_product_service(product:WebshopRequest, db: AsyncSession) -> WebshopProducts:
    return await create_product(product, db)

async def get_product_service(product_id: str, db: AsyncSession) -> WebshopProducts:
    product = await get_product_by_id(product_id, db)

    if product is None:
        raise HTTPException(status_code=404, detail=f"product id {product_id} not found")

    return product

async def update_product_service(product_id: str, updated_product: WebshopRequest, db: AsyncSession) -> WebshopProducts: 
    product = await get_product_service(product_id, db)
    
    return await update_product_by_id(product, updated_product, db)
    

async def delete_product_service(product_id: str, db: AsyncSession) -> WebshopProducts:
    product = await get_product_service(product_id, db)

    return await delete_product_by_id(product, db)

