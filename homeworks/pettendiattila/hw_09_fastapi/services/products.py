
from crud.products import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product_by_id,
    delete_product_by_id
)

from schemas import ProductRequest


async def get_all_products_service(db):
    return await get_all_products(db)


async def get_product_by_id_service(product_id: str, db):
    return await get_product_by_id(product_id, db)


async def create_product_service(product: ProductRequest, db):
    return await create_product(product, db)


async def update_product_by_id_service(
    product_id: str,
    product: ProductRequest,
    db
):
    return await update_product_by_id(product_id, product, db)


async def delete_product_by_id_service(product_id: str, db):
    return await delete_product_by_id(product_id, db)
