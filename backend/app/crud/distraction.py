from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import Distraction
from app.schemas.distraction import DistractionCreate, DistractionUpdate


def list_distractions(db: Session):
    return list_all(db, Distraction)


def get_distraction(db: Session, item_id: str):
    return get_one(db, Distraction, item_id)


def create_distraction(db: Session, payload: DistractionCreate):
    return create_one(db, Distraction, payload)


def update_distraction(db: Session, item: Distraction, payload: DistractionUpdate):
    return update_one(db, item, payload)


def delete_distraction(db: Session, item: Distraction):
    return delete_one(db, item)
