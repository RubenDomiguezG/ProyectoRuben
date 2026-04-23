from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.daily_log import create_daily_log, delete_daily_log, get_daily_log, list_daily_logs, update_daily_log
from app.db.session import get_db
from app.schemas.daily_log import DailyLogCreate, DailyLogRead, DailyLogUpdate

router = APIRouter(prefix="/daily-logs", tags=["daily_logs"])


@router.get("/", response_model=list[DailyLogRead])
def list_daily_logs_endpoint(db: Session = Depends(get_db)):
    return list_daily_logs(db)


@router.get("/{log_id}", response_model=DailyLogRead)
def get_daily_log_endpoint(log_id: str, db: Session = Depends(get_db)):
    daily_log = get_daily_log(db, log_id)
    if not daily_log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily log not found")
    return daily_log


@router.post("/", response_model=DailyLogRead, status_code=status.HTTP_201_CREATED)
def create_daily_log_endpoint(payload: DailyLogCreate, db: Session = Depends(get_db)):
    return create_daily_log(db, payload)


@router.put("/{log_id}", response_model=DailyLogRead)
def update_daily_log_endpoint(log_id: str, payload: DailyLogUpdate, db: Session = Depends(get_db)):
    daily_log = get_daily_log(db, log_id)
    if not daily_log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily log not found")
    return update_daily_log(db, daily_log, payload)


@router.delete("/{log_id}", response_model=DailyLogRead)
def delete_daily_log_endpoint(log_id: str, db: Session = Depends(get_db)):
    daily_log = get_daily_log(db, log_id)
    if not daily_log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily log not found")
    return delete_daily_log(db, daily_log)
