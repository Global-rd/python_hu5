from contextlib import asynccontextmanager
from fastapi import FastAPI

from webshop_db import Base, engine
from webshop_routers import webshop_router as webshop_router
from webshop_routers import customer_router as customer_router
from webshop_routers import order_router as order_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application started")
    yield 
    print("Application shutting down")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(webshop_router)
app.include_router(customer_router)
app.include_router(order_router)