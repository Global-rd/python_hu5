from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import Base, engine
import models
from routers.items import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application started")
    yield 
    print("Application shutting down")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
