
from contextlib import asynccontextmanager
from typing import Optional
from uuid import uuid1

from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select


# Adatbazis beallitasa
DATABASE_URL = "sqlite:///./webshop.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Termek adatmodellje
class ProductBase(SQLModel):
    item_name: str
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)
    category: Optional[str] = None


class Product(ProductBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid1()), primary_key=True)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: str


# Adatbazis tabla letrehozasa
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Webshop termeknyilvantarto",
    lifespan=lifespan
)


# Adatbazis kapcsolat
def get_session():
    with Session(engine) as session:
        yield session


# 1. Osszes termek listazasa
@app.get("/products", response_model=list[ProductRead])
def get_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products


# 2. Egy termek lekerdezese ID alapjan
@app.get("/products/{product_id}", response_model=ProductRead)
def get_product(
    product_id: str,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Termek nem talalhato"
        )

    return product


# 3. Uj termek hozzaadasa
@app.post("/products", response_model=ProductRead, status_code=201)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    new_product = Product(**product.model_dump())

    session.add(new_product)
    session.commit()
    session.refresh(new_product)

    return new_product


# 4. Termek adatainak frissitese
@app.put("/products/{product_id}", response_model=ProductRead)
def update_product(
    product_id: str,
    product_data: ProductUpdate,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Termek nem talalhato"
        )

    for key, value in product_data.model_dump().items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


# 5. Termek torlese
@app.delete("/products/{product_id}")
def delete_product(
    product_id: str,
    session: Session = Depends(get_session)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Termek nem talalhato"
        )

    session.delete(product)
    session.commit()

    return {"message": "Termek sikeresen torolve"}
