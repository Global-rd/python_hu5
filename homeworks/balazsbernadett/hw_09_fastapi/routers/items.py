from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Item
from schemas import ItemRequest, ItemResponse
from services.items import (
    list_items_service,
    create_item_service,
    get_item_service,
    update_item_service,
    delete_item_service
)

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def get_items(db: AsyncSession = Depends(get_db)) -> list[Item]:
    return await list_items_service(db)

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def add_item(item: ItemRequest, db: AsyncSession = Depends(get_db)) -> Item:
    return await create_item_service(item, db)

@router.get("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)) -> Item:
    return await get_item_service(item_id, db)


@router.put("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def update_item(
    item_id: str,
    item_update: ItemRequest,
    db: AsyncSession = Depends(get_db)
) -> Item:
    return await update_item_service(item_id, item_update, db)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, db: AsyncSession = Depends(get_db)) -> None:
    await delete_item_service(item_id, db)
    return None