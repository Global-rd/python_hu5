from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from webshop_crud import (
    create_item,
    delete_item_by_id,
    get_all_items,
    get_item_by_id,
    update_item_by_id,
    create_customer,
    get_all_customers,
    create_order
)
from webshop_models import Stock, Customer, Order
from webshop_schemas import StockRequest, CustomerRequest, OrderRequest
from email_sender import EmailSender
import os
from dotenv import load_dotenv
from starlette.concurrency import run_in_threadpool

async def list_items_service(db: AsyncSession) -> list[Stock]:
    return await get_all_items(db)

async def create_item_service(item: StockRequest, db: AsyncSession) -> Stock:
    return await create_item(item, db)

async def get_item_service(item_id: str, db: AsyncSession) -> Stock:
    item = await get_item_by_id(item_id, db)

    if item is None:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return item


async def update_item_service(item_id: str, item_update: StockRequest,
                               db:AsyncSession) -> Stock:

    item = await get_item_service(item_id, db)
    return await update_item_by_id(item, item_update, db)


async def delete_item_service(item_id: str, db:AsyncSession) -> Stock:
    item = await get_item_service(item_id, db)

    return await delete_item_by_id(item, db)


async def create_customer_service(item: CustomerRequest, db: AsyncSession) -> Customer:
    return await create_customer(item, db)


async def list_customers_service(db: AsyncSession) -> list[Customer]:
    return await get_all_customers(db)


async def place_order_service(item: OrderRequest, db: AsyncSession) -> Order:
    new_order = await create_order(item, db)

    customer = await db.get(Customer, new_order.customer_id)
    
    await run_in_threadpool(
            send_email_service,
            recipient=customer.customer_email,
            customer_name=customer.customer_name)

    return new_order

def send_email_service(recipient: str, customer_name: str):
    load_dotenv()

    #email sending:

    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email=os.environ.get("GMAIL_EMAIL"),
        sender_password=os.environ.get("GMAIL_PW")
    )

    html_body = EmailSender.render_email_template(template_path="homeworks/danielkrimer/hw_09_fastapi/email_template.html",
                                                  context={"user_name": customer_name})

    email_sender.send_email(recipients=[recipient, "daniel.krimer@gmail.com"], #nigrushid@gmail.com
                            subject="Confirm order on FastAPI Webshop",
                            body=html_body,
                            attachments=[])



