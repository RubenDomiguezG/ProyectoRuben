from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.study_session import (
    create_study_session,
    delete_study_session,
    get_study_session,
    list_study_sessions,
    update_study_session,
)
from app.db.session import get_db
from app.schemas.study_session import StudySessionCreate, StudySessionRead, StudySessionUpdate

router = APIRouter(prefix="/study-sessions", tags=["study_sessions"])


@router.get("/", response_model=list[StudySessionRead])
def list_study_sessions_endpoint(db: Session = Depends(get_db)):
    return list_study_sessions(db)


@router.get("/{item_id}", response_model=StudySessionRead)
def get_study_session_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_study_session(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study session not found")
    return item


@router.post("/", response_model=StudySessionRead, status_code=status.HTTP_201_CREATED)
def create_study_session_endpoint(payload: StudySessionCreate, db: Session = Depends(get_db)):
    return create_study_session(db, payload)


@router.put("/{item_id}", response_model=StudySessionRead)
def update_study_session_endpoint(item_id: str, payload: StudySessionUpdate, db: Session = Depends(get_db)):
    item = get_study_session(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study session not found")
    return update_study_session(db, item, payload)


@router.delete("/{item_id}", response_model=StudySessionRead)
def delete_study_session_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_study_session(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study session not found")
    return delete_study_session(db, item)
