from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from schemas import ProductRequest


async def get_all_products(db: AsyncSession) -> list[Product]:
    result = await db.execute(select(Product))  # SELECT * FROM products
    products = list(result.scalars().all())
    return products


async def get_product_by_id(product_id: str, db: AsyncSession) -> Product | None:
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    return product


async def create_product(product: ProductRequest, db: AsyncSession) -> Product:
    new_product = Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)

    return new_product


# Az update résszel elakadtam :(
# A create-hez hasonlóan próbáltam, de itt is új id-val jön létre, nem a meglévőt írja felül. :/
#
# async def update_product_by_id(product_id: str, product_update: ProductRequest, db: AsyncSession) -> Product:
#     product = Product(**product_update.model_dump())
#     db.add(product)
#     await db.commit()
#     return product
