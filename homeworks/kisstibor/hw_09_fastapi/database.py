from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base


database_path = Path(__file__).resolve().parent / "products.db"
engine = create_async_engine(f"sqlite+aiosqlite:///{database_path}")
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_db():
    """Adatbazis-sessiont biztosit egy API-kereshez."""
    async with SessionLocal() as db:
        yield db
