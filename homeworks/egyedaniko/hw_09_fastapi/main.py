from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal, Base, engine
from models import Product
from schemas import ProductCreate, ProductResponse


# Induláskor létrehozzuk a hiányzó táblákat, leálláskor lezárjuk a kapcsolatokat.
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        yield
    finally:
        await engine.dispose()


app = FastAPI(title="Product Inventory API", lifespan=lifespan)


# Közös keresés, hogy ne ismételjük a 404-es hibakezelést.
async def find_product(session: AsyncSession, product_id: str) -> Product:
    product = await session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Összes termék listázása. Üres adatbázis esetén üres listát adunk vissza.
@app.get("/products", response_model=list[ProductResponse])
async def get_products():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Product).order_by(Product.item_name))
        return result.scalars().all()


# Egy termék lekérdezése azonosító alapján.
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    async with AsyncSessionLocal() as session:
        return await find_product(session, product_id)


# Új termék: az id-t a modell generálja, a kliensnek nem kell megadnia.
@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product_data: ProductCreate):
    # Siker esetén automatikus commit, hiba esetén automatikus rollback történik.
    async with AsyncSessionLocal.begin() as session:
        product = Product(**product_data.model_dump())
        session.add(product)
        # Az INSERT lefut, és elérhetővé válik a generált id.
        await session.flush()
    return product


# PUT: a termék összes szerkeszthető adatának cseréje, az id megőrzésével.
# Az elhagyott category értéke None lesz.
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product_data: ProductCreate):
    async with AsyncSessionLocal.begin() as session:
        product = await find_product(session, product_id)
        for field, value in product_data.model_dump().items():
            setattr(product, field, value)
    return product


# Sikeres törlés után 204-es státuszt és üres választ adunk.
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str):
    async with AsyncSessionLocal.begin() as session:
        product = await find_product(session, product_id)
        await session.delete(product)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
