from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.sleep_log import create_sleep_log, delete_sleep_log, get_sleep_log, list_sleep_logs, update_sleep_log
from app.db.session import get_db
from app.schemas.sleep_log import SleepLogCreate, SleepLogRead, SleepLogUpdate

router = APIRouter(prefix="/sleep-logs", tags=["sleep_logs"])


@router.get("/", response_model=list[SleepLogRead])
def list_sleep_logs_endpoint(db: Session = Depends(get_db)):
    return list_sleep_logs(db)


@router.get("/{item_id}", response_model=SleepLogRead)
def get_sleep_log_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_sleep_log(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sleep log not found")
    return item


@router.post("/", response_model=SleepLogRead, status_code=status.HTTP_201_CREATED)
def create_sleep_log_endpoint(payload: SleepLogCreate, db: Session = Depends(get_db)):
    return create_sleep_log(db, payload)


@router.put("/{item_id}", response_model=SleepLogRead)
def update_sleep_log_endpoint(item_id: str, payload: SleepLogUpdate, db: Session = Depends(get_db)):
    item = get_sleep_log(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sleep log not found")
    return update_sleep_log(db, item, payload)


@router.delete("/{item_id}", response_model=SleepLogRead)
def delete_sleep_log_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_sleep_log(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sleep log not found")
    return delete_sleep_log(db, item)
