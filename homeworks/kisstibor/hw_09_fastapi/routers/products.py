from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Product
from schemas import ProductRequest, ProductResponse
from services.products import (
    create_product_service,
    delete_product_service,
    get_product_service,
    list_products_service,
    update_product_service,
)


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)) -> list[Product]:
    """Visszaadja az osszes termeket."""
    return await list_products_service(db)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)) -> Product:
    """Visszaadja a megadott azonositohoz tartozo termeket."""
    return await get_product_service(product_id, db)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductRequest, db: AsyncSession = Depends(get_db)) -> Product:
    """Letrehoz egy termeket a kapott adatok alapjan."""
    return await create_product_service(product, db)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: str, product: ProductRequest, db: AsyncSession = Depends(get_db)
) -> Product:
    """A megadott termek minden frissitheto adatat lecsereli."""
    return await update_product_service(product_id, product, db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)) -> Response:
    """Torli a megadott termeket, es ures valaszt ad."""
    await delete_product_service(product_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
