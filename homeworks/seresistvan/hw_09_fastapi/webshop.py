from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: str | None = None

@app.get("/items")
def list_items():
    return []