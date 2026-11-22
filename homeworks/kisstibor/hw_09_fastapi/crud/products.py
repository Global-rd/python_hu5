from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Product
from schemas import ProductRequest

async def get_all_products(db: AsyncSession) -> list[Product]:
    """Lekeri az adatbazisban tarolt osszes termeket."""
    result = await db.execute(select(Product))
    return list(result.scalars().all())

async def get_product_by_id(product_id: str, db: AsyncSession) -> Product | None:
    """Az azonositoval egyezo termeket keresi meg."""
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalar_one_or_none()

async def create_product(product: ProductRequest, db: AsyncSession) -> Product:
    """Elment egy uj termeket, majd visszaadja a letrehozott rekordot."""
    new_product = Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product

async def update_product_by_id(existing_product: Product, product_update: ProductRequest, db: AsyncSession ) -> Product:
    """Frissiti es elmenti a termek osszes modosithato mezojet."""
    existing_product.item_name = product_update.item_name
    existing_product.quantity = product_update.quantity
    existing_product.price = product_update.price
    existing_product.category = product_update.category
    await db.commit()
    await db.refresh(existing_product)
    return existing_product

async def delete_product_by_id(product: Product, db: AsyncSession) -> None:
    """Torli a megadott termeket az adatbazisbol."""
    await db.delete(product)
    await db.commit()
