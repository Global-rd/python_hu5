from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# Táblák létrehozása az adatbázisban
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Webshop Termék Nyilvántartó API")

# 1. Minden termék listázása
@app.get("/items/", response_model=List[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

# 2. Egy termék listázása id alapján
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: str, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="A termék nem található")
    return item

# 3. Egy termék hozzáadása (id automatikusan generálódik és visszakerül a válaszba)
@app.post("/items/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 4. Egy termék adatainak frissítése id alapján
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: str, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="A termék nem található")
    
    update_data = item_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
        
    db.commit()
    db.refresh(db_item)
    return db_item

# 5. Egy termék törlése id alapján
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: str, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="A termék nem található")
    
    db.delete(db_item)
    db.commit()
    return None
