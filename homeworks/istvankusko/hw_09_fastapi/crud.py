

from typing import List, Optional
from sqlalchemy.orm import Session
import models
import schemas


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
    """Retrieve a list of all items."""
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: str) -> Optional[models.Item]:
    """Retrieve a single item by its ID."""
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    """Create a new item in the database."""
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(
    db: Session, item_id: str, item_update: schemas.ItemUpdate
) -> Optional[models.Item]:
    """Update an existing item's fields by its ID."""
    db_item = get_item_by_id(db=db, item_id=item_id)
    if not db_item:
        return None

    update_data = item_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: str) -> bool:
    """Delete an item from the database by its ID."""
    db_item = get_item_by_id(db=db, item_id=item_id)
    if not db_item:
        return False

    db.delete(db_item)
    db.commit()
    return True

