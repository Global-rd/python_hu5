"""
Hozz létre egy FastAPI app-ot ami egy képzeletbeli webshop termék
nyílvántartójaként működik az alapvető CRUD endpoint-okkal.
Az adatbázis modell tartalmazza a következő oszlopokat (állíts be primary key-t is):
  id (egyedi azonosító, pl uuid1 által generált)
  item_name (pl: morzsaporszívó)
  quantity (pl: 12)
  price (pl: 24900)
  category (ez a field legyen opcionális, pl: háztartási gép)
A típusokat válaszd meg a bennük tárolt adatoknak megfelelően. Az endpoint-ok
segítségével a következőkre kell alkalmasnak lennie az app-nak:
- Minden termék listázása
- 1 termék listázása id alapján
- 1 termék hozzáadása (ne kelljen id-t megadni, de a response-ban legyen benne miután létrejött)
- 1 termék adatainak frissítése id alapján
- 1 termék törlése id alapján
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import Base, engine
from routers.products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Application started")
    yield 
    print("Application shutting down")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
