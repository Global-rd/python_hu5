from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import Base, engine
from routers.products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application startup: Database tables created.")
    yield
    print("Application shutdown: Database tables dropped.")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

app = FastAPI(lifespan=lifespan)
app.include_router(products_router)