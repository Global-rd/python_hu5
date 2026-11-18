from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from webshop_models import Stock, Customer, Order
from webshop_schemas import StockRequest, CustomerRequest, OrderRequest

async def get_all_items(db: AsyncSession) -> list[Stock]:
    result = await db.execute(select(Stock))
    items = list(result.scalars().all())
    return items

async def get_item_by_id(item_id: str, db:AsyncSession) -> Stock | None:
    result = await db.execute(select(Stock).where(Stock.item_id == item_id))
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
    
    stock = await db.get(Stock, item.item_id)

    if item.item_quantity <= 0: #Check if order quantity makes sense
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Cannot order {item.item_quantity} item.")
    elif item.item_quantity > stock.quantity: #Check if there is enough items on stock
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"There is only {stock.quantity} piece(s) of {stock.item_name} on stock, cannot order {item.item_quantity}.")
    else:
        new_order = Order(**item.model_dump(),order_value=stock.unit_price * item.item_quantity)
        db.add(new_order)
        stock.quantity -= item.item_quantity #Updating quantity of ordered item on stock
        await db.commit()
        await db.refresh(new_order)

        return new_order


async def get_all_orders(db: AsyncSession) -> list[Order]:
    result = await db.execute(select(Order))
    orders = list(result.scalars().all())
    return orders