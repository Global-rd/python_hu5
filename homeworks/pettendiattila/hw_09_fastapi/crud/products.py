
from sqlalchemy import select

from models import Product
from schemas import ProductRequest


async def get_all_products(db):
    query = select(Product)
    result = await db.execute(query)
    products = result.scalars().all()

    return products


async def get_product_by_id(product_id: str, db):
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)
    product = result.scalar_one_or_none()

    return product


async def create_product(product: ProductRequest, db):
    new_product = Product(**product.model_dump())

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


async def update_product_by_id(product_id: str, product: ProductRequest, db):
    existing_product = await get_product_by_id(product_id, db)

    if existing_product is None:
        return None

    existing_product.item_name = product.item_name
    existing_product.quantity = product.quantity
    existing_product.price = product.price
    existing_product.category = product.category

    await db.commit()
    await db.refresh(existing_product)

    return existing_product


async def delete_product_by_id(product_id: str, db):
    existing_product = await get_product_by_id(product_id, db)

    if existing_product is None:
        return None

    await db.delete(existing_product)
    await db.commit()

    return existing_product
