from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Item
from schemas import ItemRequest

async def get_all_items(db: AsyncSession) -> list[Item]:
    result = await db.execute(select(Item)) 
    items = list(result.scalars().all())
    return items

async def get_item_by_id(item_id: str, db:AsyncSession) -> Item | None:
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    return item

async def create_item(item: ItemRequest, db: AsyncSession) -> Item:
    new_item = Item(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


async def update_item_by_id(existing_item: Item, item_update: ItemRequest, db: AsyncSession) -> Item:
    for key, value in item_update.model_dump(exclude_unset=True).items():
        setattr(existing_item, key, value)

    db.add(existing_item)
    await db.commit()
    await db.refresh(existing_item)

    return existing_item


async def delete_item_by_id(item: Item, db: AsyncSession) -> Item:
    await db.delete(item)
    await db.commit()

    return item