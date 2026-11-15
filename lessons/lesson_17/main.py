from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import Base, engine
from routers.movies import router as movies_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application started")
    yield 
    print("Application shutting down")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(movies_router)