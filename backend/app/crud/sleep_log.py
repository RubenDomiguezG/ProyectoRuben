from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import SleepLog
from app.schemas.sleep_log import SleepLogCreate, SleepLogUpdate


def list_sleep_logs(db: Session):
    return list_all(db, SleepLog)


def get_sleep_log(db: Session, item_id: str):
    return get_one(db, SleepLog, item_id)


def create_sleep_log(db: Session, payload: SleepLogCreate):
    return create_one(db, SleepLog, payload)


def update_sleep_log(db: Session, item: SleepLog, payload: SleepLogUpdate):
    return update_one(db, item, payload)


def delete_sleep_log(db: Session, item: SleepLog):
    return delete_one(db, item)
