from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./webshop.db" #set database(SQLite)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


#set database model (SQLAlchemy)
class ItemDB(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True, index=True)  # Primary key automatically increase up
  item_name = Column(String, index=True, nullable=False)
  quantity = Column(Integer, nullable=False)
  price = Column(Float, nullable=False)
  category = Column(String, index=True, nullable=False)


#Lifespan, firstly load th db, after that the app
@asynccontextmanager
async def lifespan(app: FastAPI):
  Base.metadata.create_all(bind=engine)
  print("Database loaded!")
  yield
  print("The app was stopped")


# FastAPI
app = FastAPI(title="Fictive_Shop 🛒", lifespan=lifespan)

#Validation and Response
class ItemCreate(BaseModel):
  item_name: str
  quantity: int
  price: float
  category: str

class ItemUpdate(BaseModel):
  item_name: Optional[str] = None
  quantity: Optional[int] = None
  price: Optional[float] = None
  category: Optional[str] = None

class ItemResponse(BaseModel):
  id: int
  item_name: str
  quantity: int
  price: float
  category: str

  class Config:
    from_attributes = True

# Databease connection
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/", include_in_schema=False)
def root():
  return RedirectResponse(url="/docs") #redirecting url, directly loaded /docs

# CREATE: add item wait without ID but add back with ID
@app.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
  db_item = ItemDB(
      item_name=item.item_name,
      quantity=item.quantity,
      price=item.price,
      category=item.category,
  )
  db.add(db_item)
  db.commit()
  db.refresh(db_item)
  return db_item


# List all product
@app.get("/items/", response_model=List[ItemResponse])
def read_all_items(db: Session = Depends(get_db)):
  return db.query(ItemDB).all()


# List product by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
  db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
  if db_item is None:
    raise HTTPException(status_code=404, detail="Product not found.")
  return db_item


# Update product by ID
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
  db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
  if db_item is None:
    raise HTTPException(status_code=404, detail="Product not found.")

  update_data = item.model_dump(exclude_unset=True)
  for key, value in update_data.items():
    setattr(db_item, key, value)

  db.commit()
  db.refresh(db_item)
  return db_item


# Delete product by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
  db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
  if db_item is None:
    raise HTTPException(status_code=404, detail="Product not found.")

  db.delete(db_item)
  db.commit()
  return {"message": f"The {item_id} item was deleted"}