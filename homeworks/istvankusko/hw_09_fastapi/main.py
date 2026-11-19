

from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import crud
from database import Base, engine, get_db
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Webshop Inventory API",
    description="CRUD API for managing webshop product inventory.",
    version="1.0.0",
)


@app.get("/items/", response_model=List[schemas.ItemResponse])
def read_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """Retrieve all items from the inventory."""
    return crud.get_items(db=db, skip=skip, limit=limit)


@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: str, db: Session = Depends(get_db)):
    """Retrieve a single item by its ID."""
    db_item = crud.get_item_by_id(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return db_item


@app.post(
    "/items/",
    response_model=schemas.ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Add a new item to the inventory."""
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(
    item_id: str, item: schemas.ItemUpdate, db: Session = Depends(get_db)
):
    """Update an existing item's details by its ID."""
    db_item = crud.update_item(db=db, item_id=item_id, item_update=item)
    if db_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return db_item


@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
def delete_item(item_id: str, db: Session = Depends(get_db)):
    """Delete an item from the inventory by its ID."""
    success = crud.delete_item(db=db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return {"message": "Item successfully deleted"}

