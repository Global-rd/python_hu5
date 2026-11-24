from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from webshop_crud import (
    create_stock_item,
    delete_stock_item_by_id,
    get_all_stock_items,
    get_stock_item_by_id,
    update_stock_item_by_id,
    create_product_item,
    get_product_item_by_id,
    delete_product_item_by_id,
    get_all_product_items,
    update_product_item_by_id,
    create_customer,
    get_all_customers,
    create_order,
    get_all_orders)
from webshop_models import Stock, Customer, Order, Product
from webshop_schemas import StockRequest, CustomerRequest, OrderRequest, ProductRequest
from email_sender import EmailSender
import os
from dotenv import load_dotenv
from starlette.concurrency import run_in_threadpool

async def list_stock_items_service(db: AsyncSession) -> list[Stock]:
    return await get_all_stock_items(db)

async def create_stock_item_service(item: StockRequest, db: AsyncSession) -> Stock:
    return await create_stock_item(item, db)

async def get_stock_item_service(item_id: str, db: AsyncSession) -> Stock:
    item = await get_stock_item_by_id(item_id, db)

    if item is None:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return item


async def update_stock_item_service(item_id: str, item_update: StockRequest,
                               db:AsyncSession) -> Stock:
    item = await get_stock_item_service(item_id, db)

    if item is None:
            raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")
    
    return await update_stock_item_by_id(item, item_update, db)


async def delete_stock_item_service(item_id: str, db:AsyncSession) -> Stock:
    item = await get_stock_item_service(item_id, db)

    if item is None:
            raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return await delete_stock_item_by_id(item, db)


async def list_product_items_service(db: AsyncSession) -> list[Product]:
    return await get_all_product_items(db)

async def create_product_item_service(item: ProductRequest, db: AsyncSession) -> Product:
    return await create_product_item(item, db)


async def get_product_item_service(item_id: str, db: AsyncSession) -> Product:
    item = await get_product_item_by_id(item_id, db)

    if item is None:
        raise HTTPException(status_code=404, detail=f"Product id {item_id} not found")

    return item


async def update_product_item_service(item_id: str, item_update: ProductRequest,
                               db:AsyncSession) -> Product:
    item = await get_product_item_service(item_id, db)

    if item is None:
            raise HTTPException(status_code=404, detail=f"Product id {item_id} not found")
    
    return await update_product_item_by_id(item, item_update, db)


async def delete_product_item_service(item_id: str, db:AsyncSession) -> Product:
    item = await get_product_item_service(item_id, db)

    if item is None:
            raise HTTPException(status_code=404, detail=f"Product id {item_id} not found")

    return await delete_product_item_by_id(item, db)


async def create_customer_service(item: CustomerRequest, db: AsyncSession) -> Customer:
    return await create_customer(item, db)


async def list_customers_service(db: AsyncSession) -> list[Customer]:
    return await get_all_customers(db)


async def place_order_service(item: OrderRequest, db: AsyncSession) -> Order:
    new_order = await create_order(item, db)

    stmt = (select(Order)
        .options(selectinload(Order.items))
        .where(Order.order_id == new_order.order_id))

    result = await db.execute(stmt)
    new_order = result.scalar_one()

    customer = await db.get(Customer, new_order.customer_id)
    
    await run_in_threadpool(
            send_confirmation_email_service,
            recipient=customer.customer_email,
            customer_name=customer.customer_name)

    return new_order


async def list_orders_service(db: AsyncSession) -> list[Order]:
    return await get_all_orders(db)


def send_confirmation_email_service(recipient: str, customer_name: str):
    load_dotenv()

    #email sending:

    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email=os.environ.get("EMAIL"),
        sender_password=os.environ.get("EMAIL_PW")
    )

    html_body = EmailSender.render_email_template(template_path="confirmation_email_template.html",
                                                  context={"customer_name": customer_name})

    email_sender.send_email(recipients=[recipient],
                            subject="Confirmation of your order from FastAPI Webshop",
                            body=html_body,
                            attachments=[])



