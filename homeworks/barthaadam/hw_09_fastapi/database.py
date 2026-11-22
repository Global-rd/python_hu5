from pathlib import Path
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine


# Az adatbázisfájl a Python-fájlok mellett lesz.
DATABASE_FILE = Path(__file__).resolve().with_name("webshop.db")

DATABASE_URL = f"sqlite:///{DATABASE_FILE.as_posix()}"


# Az engine kezeli az adatbázishoz való kapcsolódást.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables() -> None:
    """Létrehozza a hiányzó adatbázistáblákat."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Adatbázis-munkamenetet biztosít egy kéréshez."""
    with Session(engine) as session:
        yield session