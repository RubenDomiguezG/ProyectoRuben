from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.distraction import create_distraction, delete_distraction, get_distraction, list_distractions, update_distraction
from app.db.session import get_db
from app.schemas.distraction import DistractionCreate, DistractionRead, DistractionUpdate

router = APIRouter(prefix="/distractions", tags=["distractions"])


@router.get("/", response_model=list[DistractionRead])
def list_distractions_endpoint(db: Session = Depends(get_db)):
    return list_distractions(db)


@router.get("/{item_id}", response_model=DistractionRead)
def get_distraction_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_distraction(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Distraction not found")
    return item


@router.post("/", response_model=DistractionRead, status_code=status.HTTP_201_CREATED)
def create_distraction_endpoint(payload: DistractionCreate, db: Session = Depends(get_db)):
    return create_distraction(db, payload)


@router.put("/{item_id}", response_model=DistractionRead)
def update_distraction_endpoint(item_id: str, payload: DistractionUpdate, db: Session = Depends(get_db)):
    item = get_distraction(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Distraction not found")
    return update_distraction(db, item, payload)


@router.delete("/{item_id}", response_model=DistractionRead)
def delete_distraction_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_distraction(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Distraction not found")
    return delete_distraction(db, item)
