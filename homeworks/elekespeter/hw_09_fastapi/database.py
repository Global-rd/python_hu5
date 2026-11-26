from pathlib import Path
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# Az adatbázisfájl mindig a database.py mellé kerül, bárhonnan indítjuk az appot
# (az órán "./movies.db" volt, ami a terminál aktuális mappájától függ).
DB_PATH = Path(__file__).parent / "products.db"
DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH.as_posix()}"

# echo=True esetén minden SQL-utasítás kiíródik a terminálba (hibakereséshez hasznos)
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Minden kéréshez egy adatbázis-session-t ad (FastAPI Depends)."""
    async with AsyncSessionLocal() as session:
        yield session
