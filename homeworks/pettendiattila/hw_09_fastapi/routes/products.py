
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import ProductRequest, ProductResponse

from services.products import (
    get_all_products_service,
    get_product_by_id_service,
    create_product_service,
    update_product_by_id_service,
    delete_product_by_id_service
)


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    return await get_all_products_service(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)):
    product = await get_product_by_id_service(product_id, db)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductRequest, db: AsyncSession = Depends(get_db)):
    return await create_product_service(product, db)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: str,
    product: ProductRequest,
    db: AsyncSession = Depends(get_db)
):
    updated_product = await update_product_by_id_service(product_id, product, db)

    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_id: str,
    db: AsyncSession = Depends(get_db)
) -> None:
    deleted_product = await delete_product_by_id_service(product_id, db)

    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return None
