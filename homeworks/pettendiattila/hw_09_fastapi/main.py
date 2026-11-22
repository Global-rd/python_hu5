from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine, Base
from models import Product
from routes.products import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(router)