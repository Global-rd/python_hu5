from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import WebshopProducts
from schemas import WebshopRequest

async def get_all_products(db: AsyncSession) -> list[WebshopProducts]:
    result = await db.execute(select(WebshopProducts))
    products = list(result.scalars().all())
    return products

async def get_product_by_id(product_id: str, db: AsyncSession) -> WebshopProducts | None:
    result = await db.execute(select(WebshopProducts).where(WebshopProducts.id == product_id))
    product = result.scalar_one_or_none()
    return product

async def create_product(product: WebshopRequest, db: AsyncSession) -> WebshopProducts:
    new_product = WebshopProducts(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product

async def update_product_by_id(existing_product: WebshopProducts, updated_product: WebshopRequest, db: AsyncSession) -> WebshopProducts:
    for key, value in updated_product.model_dump(exclude_unset=True).items():
        setattr(existing_product, key, value)
    db.add(existing_product)
    await db.commit()
    await db.refresh(existing_product)

    return existing_product


async def delete_product_by_id(product: WebshopProducts, db: AsyncSession) -> WebshopProducts:
    await db.delete(product)
    await db.commit()

    return product

