"""HAZI FELADAT 09 FASTAPI"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import Base, engine
from routers.products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Letrehozza az adatbazist inditaskor, majd leallasnal lezarja a kapcsolatot."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
