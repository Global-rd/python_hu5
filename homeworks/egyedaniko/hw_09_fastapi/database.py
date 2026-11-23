from pathlib import Path

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


# Az adatbázis a Python-fájlok mellett jön létre, az indítás helyétől függetlenül.
DATABASE_FILE = Path(__file__).resolve().parent / "products.db"
DATABASE_URL = URL.create("sqlite+aiosqlite", database=str(DATABASE_FILE))

engine = create_async_engine(DATABASE_URL, echo=False)

# Minden kérés saját munkamenetet használ.
# A mentés után is elérhetők maradnak a betöltött mezők.
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


# Az adatbázismodellek közös ősosztálya.
class Base(DeclarativeBase):
    pass
