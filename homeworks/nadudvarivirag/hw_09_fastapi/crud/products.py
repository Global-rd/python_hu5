# itt írjuk meg hogy a pythonból sql kód legyen és fordítva. Kommunikáljon az adatbázissal
# itt a response azért nem kell, mert az adatbázissal dolgozunk

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Product
from schemas import ProductRequest

# itt feladatot adunk az adatbázisnak, ezért várni kell --> async
# azt a sessiont kell megkapnia, amik a változtatásokat tartalmazza
# await mert lehet hogy várakozni kell majd az adatbázisra. Ez a lényeg
# Így tudja kiszolgálni a többi requestet "párhuzamosan"
# fileterezés nélkül kérem le az adatokat --> select * from
# a vissza adott listát át kell alakítani a sqlalchemy scalarsával. ezután lesz vissza adható

async def get_all_products(db: AsyncSession) -> list[Product]:           
    result = await db.execute(select(Product))
    products = list(result.scalars().all())
    return products                        
                                                        

async def get_product_by_id(Product_id: str, db: AsyncSession,) -> Product | None:
    result = await db.execute(select(Product).where(Product.id == Product_id))
    product = result.scalar_one_or_none()
    return product


async def insert_product(product: ProductRequest, db: AsyncSession) -> Product:
    new_product = Product(**product.model_dump())
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product) #itt kerül be az id
    
    return new_product 

async def update_product_by_id(existing_product: Product, product_update: ProductRequest, db: AsyncSession) -> Product:
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(existing_product, key, value)

    db.add(existing_product)
    await db.commit()
    await db.refresh(existing_product)

    return existing_product


async def delete_product_by_id(product: Product, db: AsyncSession) -> Product:
    await db.delete(product)
    await db.commit()

    return product

