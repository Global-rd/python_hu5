from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Product
from schemas import ProductRequest, ProductResponse
from crud.products import get_all_products, get_product_by_id, create_product

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_products(db: AsyncSession = Depends(get_db)) -> list[Product]:
    return await get_all_products(db)


# nem létező id-nél 500 Internal Server Error jön :/
@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)) -> Product:
    return await get_product_by_id(product_id, db)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductRequest, db: AsyncSession = Depends(get_db)) -> Product:
    return await create_product(product, db)


# Az update és delete feladatokat nem tudtam megcsinálni.
