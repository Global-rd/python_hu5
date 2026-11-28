from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from schemas import ProductRequest

# A CRUD réteg csak az adatbázissal beszél: nem dönt, nem dob HTTP-hibát.


async def get_all_products(db: AsyncSession) -> list[Product]:
    result = await db.execute(select(Product))  # SELECT * FROM products
    return list(result.scalars().all())


async def get_product_by_id(product_id: str, db: AsyncSession) -> Product | None:
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()


async def create_product(product: ProductRequest, db: AsyncSession) -> Product:
    new_product = Product(**product.model_dump())  # az id-t a modell default-ja generálja
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)  # visszaolvassuk, így benne lesz a generált id
    return new_product


async def update_product(existing_product: Product, product_update: ProductRequest,
                         db: AsyncSession) -> Product:
    # A kérésben megadott mezőkkel felülírjuk a meglévő termék adatait
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(existing_product, key, value)

    db.add(existing_product)
    await db.commit()
    await db.refresh(existing_product)
    return existing_product


async def delete_product(product: Product, db: AsyncSession) -> Product:
    await db.delete(product)
    await db.commit()
    return product
