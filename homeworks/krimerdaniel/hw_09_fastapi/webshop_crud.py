from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from webshop_models import Stock, Customer, Order
from webshop_schemas import StockRequest, CustomerRequest, OrderRequest

async def get_all_items(db: AsyncSession) -> list[Stock]:
    result = await db.execute(select(Stock))
    items = list(result.scalars().all())
    return items

async def get_item_by_id(item_id: str, db:AsyncSession) -> Stock | None:
    result = await db.execute(select(Stock).where(Stock.id == item_id))
    item = result.scalar_one_or_none()
    return item

async def create_item(item: StockRequest, db: AsyncSession) ->Stock:
    new_item = Stock(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


async def update_item_by_id(existing_item: Stock, item_update: StockRequest, db: AsyncSession) -> Stock:
    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(existing_item, key, value)

    db.add(existing_item)
    await db.commit()
    await db.refresh(existing_item)

    return existing_item


async def delete_item_by_id(item: Stock, db: AsyncSession) -> Stock:
    await db.delete(item)
    await db.commit()

    return item


async def create_customer(item: CustomerRequest, db: AsyncSession) ->Customer:
    new_customer = Customer(**item.model_dump())
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)

    return new_customer


async def get_all_customers(db: AsyncSession) -> list[Customer]:
    result = await db.execute(select(Customer))
    customers = list(result.scalars().all())
    return customers


async def create_order(item: OrderRequest, db: AsyncSession) -> Order:
    new_order = Order(**item.model_dump())
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return new_order