from typing import Optional, List
from fastapi import APIRouter, status, Depends, Response

# Schemas
import app.schemas.items as schema

# Models
import app.models.items as model

# Database:
from sqlalchemy.orm import Session
from config.database import get_db

# Routes
router = APIRouter(tags=["Items"])


@router.get(
    path="/items",
    status_code=status.HTTP_200_OK,
    response_model=List[schema.Item],
)
def get_all_items(
    db: Session = Depends(get_db)
):
    """
    Documentation:
    """
    items = db.query(model.Item).all()
    return items


@router.get(
    path="/items/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=schema.Item,
)
def get_an_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Documentation
    """

    item = db.query(model.Item).filter_by(id=item_id).first()

    return item


@router.post(
    path="/items",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.Item,
)
def create_item(
    item: schema.InputItem,
    db: Session = Depends(get_db),
):
    """
    Documentation:
    """
    new_item = model.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.put(
    path="/items/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=schema.Item,
)
def update_item(
    item_id: int,
    updated_item: schema.InputItem,
    db: Session = Depends(get_db)
):
    """
    Documentation:
    """

    item_query = db.query(model.Item).filter_by(id=item_id)

    item = item_query.first()

    item_query.update(updated_item.dict(), synchronize_session=False)

    db.commit()

    return item


@router.delete(
    path="/items/{item_id}",
    # status_code=status.HTTP_204_NO_CONTENT
)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    """
    Documentation:
    """
    item_query = db.query(model.Item).filter_by(id=item_id)

    # item = item_query.first()

    item_query.delete(synchronize_session=False)

    db.commit()

    return {"msg": "ok", "data": f'Item ID:{item_id} has been removed.'}
