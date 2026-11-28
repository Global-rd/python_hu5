from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from webshop_models import Stock, Product, Customer, Order, OrderLineItem
from webshop_schemas import StockRequest, ProductRequest, CustomerRequest, OrderRequest

async def get_all_stock_items(db: AsyncSession) -> list[Stock]:
    result = await db.execute(select(Stock))
    items = list(result.scalars().all())
    return items

async def get_stock_item_by_id(item_id: str, db:AsyncSession) -> Stock | None:
    result = await db.execute(select(Stock).where(Stock.stock_id == item_id))
    item = result.scalar_one_or_none()
    return item

async def create_stock_item(item: StockRequest, db: AsyncSession) ->Stock:
    new_item = Stock(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


async def update_stock_item_by_id(existing_item: Stock, item_update: StockRequest, db: AsyncSession) -> Stock:
    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(existing_item, key, value)

    db.add(existing_item)
    await db.commit()
    await db.refresh(existing_item)

    return existing_item


async def delete_stock_item_by_id(item: Stock, db: AsyncSession) -> Stock:
    await db.delete(item)
    await db.commit()

    return item


async def create_product_item(item: ProductRequest, db: AsyncSession) ->Product:
    new_item = Product(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


async def get_product_item_by_id(item_id: str, db:AsyncSession) -> Product | None:
    result = await db.execute(select(Product).where(Product.product_id == item_id))
    item = result.scalar_one_or_none()
    return item


async def get_all_product_items(db: AsyncSession) -> list[Product]:
    result = await db.execute(select(Product))
    items = list(result.scalars().all())
    return items


async def update_product_item_by_id(existing_item: Product, item_update: ProductRequest, db: AsyncSession) -> Product:
    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(existing_item, key, value)

    db.add(existing_item)
    await db.commit()
    await db.refresh(existing_item)

    return existing_item


async def delete_product_item_by_id(item: Product, db: AsyncSession) -> Product:
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
    
    customer = await db.get(Customer, item.customer_id)

    if customer is None:
        raise HTTPException(status_code=404, detail=f"Customer {item.customer_id} does not exist.")

    try:

        new_order = Order(customer_id=item.customer_id)

        db.add(new_order)

        for item in item.items:

            product = await db.get(Product, item.product_id)

            if product is None:
                raise HTTPException(status_code=404, detail=f"Product {item.product_id} does not exist.")

            stock_result = await db.execute(select(Stock).where(Stock.product_id == product.product_id).with_for_update())

            stock = stock_result.scalar_one_or_none()

            if stock is None:
                raise HTTPException(status_code=404, detail=f"No stock record for {product.product_name}.")

            if item.item_quantity > stock.quantity:
                raise HTTPException(status_code=409, detail=(f"Only {stock.quantity} piece(s) of {product.product_name} available."))

            line_value = (product.unit_price * item.item_quantity)

            new_line_item = OrderLineItem(
                order=new_order,
                product_id=product.product_id,
                item_quantity=item.item_quantity,
                unit_price=product.unit_price,
                order_value=line_value
            )

            db.add(new_line_item)

            stock.quantity -= item.item_quantity

        await db.commit()
        await db.refresh(new_order)

        return new_order

    except Exception:
        await db.rollback()
        raise


async def get_all_orders(db: AsyncSession) -> list[Order]:
    result = await db.execute(select(Order))
    orders = list(result.scalars().all())
    return orders



