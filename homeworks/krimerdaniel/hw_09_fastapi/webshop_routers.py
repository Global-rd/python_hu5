from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from webshop_db import get_db
from webshop_models import Stock, Customer, Order
from webshop_schemas import (
    StockRequest,
    StockResponse,
    CustomerRequest,
    CustomerResponse,
    OrderRequest,
    OrderResponse
)
from webshop_services import (
    list_items_service,
    create_item_service,
    get_item_service,
    update_item_service,
    delete_item_service,
    create_customer_service,
    list_customers_service,
    place_order_service
)

webshop_router = APIRouter(
    prefix="/webshop",
    tags=["webshop"]
)

@webshop_router.get("/", response_model=list[StockResponse], status_code=status.HTTP_200_OK)
async def get_items(db: AsyncSession = Depends(get_db)) -> list[Stock]:
    return await list_items_service(db)

@webshop_router.post("/", response_model=StockResponse, status_code=status.HTTP_201_CREATED)
async def add_item(item: StockRequest, db: AsyncSession = Depends(get_db)) -> Stock:
    return await create_item_service(item, db)

@webshop_router.get("/{item_id}", response_model=StockResponse, status_code=status.HTTP_200_OK)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)) -> Stock:
    return await get_item_service(item_id, db)


@webshop_router.put("/{item_id}", response_model=StockResponse, status_code=status.HTTP_200_OK)
async def update_item(
    item_id: str,
    item_update: StockRequest,
    db: AsyncSession = Depends(get_db)
) -> Stock:
    return await update_item_service(item_id, item_update, db)

@webshop_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, db: AsyncSession = Depends(get_db)) -> None:
    await delete_item_service(item_id, db)
    return None


customer_router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)

@customer_router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
async def add_customer(item: CustomerRequest, db: AsyncSession = Depends(get_db)) -> Customer:
    return await create_customer_service(item, db)

@customer_router.get("/", response_model=list[CustomerResponse], status_code=status.HTTP_200_OK)
async def get_customers(db: AsyncSession = Depends(get_db)) -> list[Customer]:
    return await list_customers_service(db)


order_router = APIRouter(
    prefix="/order",
    tags=["order"]
)

@order_router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def place_order(item: OrderRequest, db: AsyncSession = Depends(get_db)) -> Stock:
    return await place_order_service(item, db)
