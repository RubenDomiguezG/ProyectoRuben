from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import DailyLog
from app.schemas.daily_log import DailyLogCreate, DailyLogUpdate


def list_daily_logs(db: Session):
    return db.query(DailyLog).order_by(DailyLog.log_date.desc()).all()


def get_daily_log(db: Session, log_id: str):
    return get_one(db, DailyLog, log_id)


def create_daily_log(db: Session, payload: DailyLogCreate):
    return create_one(db, DailyLog, payload)


def update_daily_log(db: Session, daily_log: DailyLog, payload: DailyLogUpdate):
    return update_one(db, daily_log, payload)


def delete_daily_log(db: Session, daily_log: DailyLog):
    return delete_one(db, daily_log)
