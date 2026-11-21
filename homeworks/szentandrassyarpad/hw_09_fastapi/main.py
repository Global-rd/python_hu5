from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import Base, engine
from routers.items import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:      # el kell indítania illetve létrehoznia az adatbázist ha még nincs meg. engine: ld database.py
        await conn.run_sync(Base.metadata.create_all) # hozzon létre minden olyan táblát modelt ami a Base-től örököl
    print("Application started")
    yield # ez engedi át a FastAPI-nak a futást
    print("Application shutting down")
    await engine.dispose()     #a végén mindenkapcsolatot bontunk az adatbázissal

app = FastAPI(lifespan=lifespan)
app.include_router(items_router) # átadom az appnak az endpointokat. 
