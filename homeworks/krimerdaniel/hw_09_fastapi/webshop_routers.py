from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from webshop_db import get_db
from webshop_models import Stock, Customer, Order, Product
from webshop_schemas import (
    StockRequest,
    StockResponse,
    CustomerRequest,
    CustomerResponse,
    OrderRequest,
    OrderResponse,
    ProductRequest,
    ProductResponse
)
from webshop_services import (
    list_stock_items_service,
    create_stock_item_service,
    get_stock_item_service,
    update_stock_item_service,
    delete_stock_item_service,
    list_product_items_service,
    create_product_item_service,
    get_product_item_service,
    update_product_item_service,
    delete_product_item_service,
    create_customer_service,
    list_customers_service,
    place_order_service,
    list_orders_service
)

stock_router = APIRouter(
    prefix="/stock",
    tags=["stock"]
)

@stock_router.get("/", response_model=list[StockResponse], status_code=status.HTTP_200_OK)
async def get_stock_items(db: AsyncSession = Depends(get_db)) -> list[Stock]:
    return await list_stock_items_service(db)

@stock_router.post("/", response_model=StockResponse, status_code=status.HTTP_201_CREATED)
async def add_stock_item(item: StockRequest, db: AsyncSession = Depends(get_db)) -> Stock:
    return await create_stock_item_service(item, db)

@stock_router.get("/{item_id}", response_model=StockResponse, status_code=status.HTTP_200_OK)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)) -> Stock:
    return await get_stock_item_service(item_id, db)


@stock_router.put("/{item_id}", response_model=StockResponse, status_code=status.HTTP_200_OK)
async def update_stock_item(
    item_id: str,
    item_update: StockRequest,
    db: AsyncSession = Depends(get_db)
) -> Stock:
    return await update_stock_item_service(item_id, item_update, db)

@stock_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_stock_item(item_id: str, db: AsyncSession = Depends(get_db)) -> None:
    await delete_stock_item_service(item_id, db)
    return None


product_router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@product_router.get("/", response_model=list[ProductResponse], status_code=status.HTTP_200_OK)
async def get_product_items(db: AsyncSession = Depends(get_db)) -> list[Product]:
    return await list_product_items_service(db)

@product_router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product_item(item: ProductRequest, db: AsyncSession = Depends(get_db)) -> Product:
    return await create_product_item_service(item, db)

@product_router.get("/{item_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product_item(item_id: str, db: AsyncSession = Depends(get_db)) -> Product:
    return await get_product_item_service(item_id, db)


@product_router.put("/{item_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product_item(
    item_id: str,
    item_update: ProductRequest,
    db: AsyncSession = Depends(get_db)
) -> Product:
    return await update_product_item_service(item_id, item_update, db)

@product_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_item(item_id: str, db: AsyncSession = Depends(get_db)) -> None:
    await delete_product_item_service(item_id, db)
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
async def place_order(item: OrderRequest, db: AsyncSession = Depends(get_db)) -> Order:
    return await place_order_service(item, db)

@order_router.get("/", response_model=list[OrderResponse], status_code=status.HTTP_200_OK)
async def get_orders(db: AsyncSession = Depends(get_db)) -> list[Order]:
    return await list_orders_service(db)



