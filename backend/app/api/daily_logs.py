from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.daily_log import (
    create_daily_log,
    create_daily_log_full,
    delete_daily_log,
    get_daily_log,
    get_daily_log_full_by_date,
    get_daily_log_full_by_id,
    list_daily_logs,
    update_daily_log,
)
from app.db.session import get_db
from app.schemas.daily_log import DailyLogCreate, DailyLogRead, DailyLogUpdate
from app.schemas.daily_log_full import DailyLogFullCreate, DailyLogFullRead

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


@router.post("/full", response_model=DailyLogFullRead, status_code=status.HTTP_201_CREATED)
def create_daily_log_full_endpoint(payload: DailyLogFullCreate, db: Session = Depends(get_db)):
    created = create_daily_log_full(db, payload)
    return {
        "daily_log": created,
        "sleep_log": created.sleep_log,
        "study_sessions": created.study_sessions,
        "workouts": created.workouts,
        "distractions": created.distractions,
    }


@router.get("/full/{log_id}", response_model=DailyLogFullRead)
def get_daily_log_full_endpoint(log_id: str, db: Session = Depends(get_db)):
    daily_log = get_daily_log_full_by_id(db, log_id)
    if not daily_log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily log full not found")
    return {
        "daily_log": daily_log,
        "sleep_log": daily_log.sleep_log,
        "study_sessions": daily_log.study_sessions,
        "workouts": daily_log.workouts,
        "distractions": daily_log.distractions,
    }


@router.get("/full/by-date/{log_date}", response_model=DailyLogFullRead)
def get_daily_log_full_by_date_endpoint(log_date: date, db: Session = Depends(get_db)):
    daily_log = get_daily_log_full_by_date(db, log_date)
    if not daily_log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Daily log full not found")
    return {
        "daily_log": daily_log,
        "sleep_log": daily_log.sleep_log,
        "study_sessions": daily_log.study_sessions,
        "workouts": daily_log.workouts,
        "distractions": daily_log.distractions,
    }


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
