from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import WebshopProducts
from schemas import WebshopRequest, WebshopResponse
from services.webshop import (
    list_products_sevice,
    create_product_service,
    get_product_service,
    delete_product_service,
    update_product_service
)

webshop_router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@webshop_router.get("/", response_model=list[WebshopResponse], status_code=status.HTTP_200_OK)
async def get_products(db: AsyncSession = Depends(get_db)) -> list [WebshopProducts]:
    return await list_products_sevice(db)

@webshop_router.post("/", response_model=WebshopResponse, status_code=status.HTTP_201_CREATED)
async def add_product(product: WebshopRequest, db:AsyncSession = Depends(get_db)) -> WebshopProducts:
    return await create_product_service(product, db)

@webshop_router.get("/{product_id}", response_model=WebshopResponse, status_code=status.HTTP_200_OK)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)) -> WebshopProducts:
    return await get_product_service(product_id, db)


@webshop_router.put("/{product_id}", response_model=WebshopResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: str, updated_product: WebshopRequest, db: AsyncSession = Depends(get_db)) -> WebshopProducts:
    return await update_product_service(product_id, updated_product, db)

@webshop_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)) -> None:
    await delete_product_service(product_id, db)
    return None