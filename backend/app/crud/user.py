from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import User
from app.schemas.user import UserCreate, UserUpdate


def list_users(db: Session):
    return list_all(db, User)


def get_user(db: Session, user_id: str):
    return get_one(db, User, user_id)


def create_user(db: Session, payload: UserCreate):
    return create_one(db, User, payload)


def update_user(db: Session, user: User, payload: UserUpdate):
    return update_one(db, user, payload)


def delete_user(db: Session, user: User):
    return delete_one(db, user)
