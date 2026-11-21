from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from crud.items import (
    create_item,
    delete_item_by_id,
    get_all_items,
    get_item_by_id,
    update_item_by_id
)
from models import Item
from schemas import ItemRequest

async def list_items_service(db: AsyncSession) -> list[Item]:
    return await get_all_items(db)

async def create_item_service(item: ItemRequest, db: AsyncSession) -> Item:
    return await create_item(item, db)

async def get_item_service(item_id: str, db: AsyncSession) -> Item:
    item = await get_item_by_id(item_id, db)

    if item is None:
        raise HTTPException(status_code=404, detail=f"Item id {item_id} not found")

    return item


async def update_item_service(item_id: str, item_update: ItemRequest,
                               db:AsyncSession) -> Item:

    item = await get_item_service(item_id, db)
    return await update_item_by_id(item, item_update, db)

async def delete_item_service(item_id: str, db:AsyncSession) -> Item:
    item = await get_item_service(item_id, db)
    return await delete_item_by_id(item, db)
