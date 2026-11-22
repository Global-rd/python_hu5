from contextlib import asynccontextmanager
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import Item, ItemInput, ItemOutput


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Az alkalmazás indulásakor létrehozzuk a hiányzó táblákat.
    create_db_and_tables()
    yield


app = FastAPI(
    title="Webshop terméknyilvántartó",
    description="Termékek listázása, hozzáadása, módosítása és törlése.",
    version="1.0.0",
    lifespan=lifespan,
)


# 1. Minden termék listázása
@app.get(
    "/items",
    response_model=list[ItemOutput],
    summary="Minden termék listázása",
)
def list_items(
    session: Session = Depends(get_session),
) -> list[Item]:

    return session.exec(select(Item)).all()


# 2. Egy termék lekérése azonosító alapján
@app.get(
    "/items/{item_id}",
    response_model=ItemOutput,
    summary="Egy termék lekérése",
)
def get_item(
    item_id: UUID,
    session: Session = Depends(get_session),
) -> Item:

    item = session.get(Item, item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="A termék nem található.",
        )

    return item


# 3. Új termék hozzáadása
@app.post(
    "/items",
    response_model=ItemOutput,
    status_code=status.HTTP_201_CREATED,
    summary="Új termék hozzáadása",
)
def create_item(
    item_data: ItemInput,
    session: Session = Depends(get_session),
) -> Item:

    # Az Item létrehozásakor az id automatikusan keletkezik.
    item = Item.model_validate(item_data)

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


# 4. Egy termék módosítása azonosító alapján
@app.put(
    "/items/{item_id}",
    response_model=ItemOutput,
    summary="Egy termék teljes módosítása",
)
def update_item(
    item_id: UUID,
    item_data: ItemInput,
    session: Session = Depends(get_session),
) -> Item:

    item = session.get(Item, item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="A termék nem található.",
        )

    # A termék adatait lecseréljük a beküldött értékekre.
    # Az id változatlan marad.
    item.item_name = item_data.item_name
    item.quantity = item_data.quantity
    item.price = item_data.price
    item.category = item_data.category

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


# 5. Egy termék törlése azonosító alapján
@app.delete(
    "/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Egy termék törlése",
)
def delete_item(
    item_id: UUID,
    session: Session = Depends(get_session),
) -> Response:

    item = session.get(Item, item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="A termék nem található.",
        )

    session.delete(item)
    session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)