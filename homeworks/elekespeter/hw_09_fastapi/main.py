from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from routers.products import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Induláskor létrehozza a táblákat, ha még nem léteznek
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application started")
    yield
    print("Application shutting down")
    await engine.dispose()


app = FastAPI(
    title="Webshop Product Inventory API",
    description="Képzeletbeli webshop termék-nyilvántartója CRUD végpontokkal (9. házi).",
    lifespan=lifespan,
)
app.include_router(products_router)
