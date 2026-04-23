from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.user import create_user, delete_user, get_user, list_users, update_user
from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserRead])
def list_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)


@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: str, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload)


@router.put("/{user_id}", response_model=UserRead)
def update_user_endpoint(user_id: str, payload: UserUpdate, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_user(db, user, payload)


@router.delete("/{user_id}", response_model=UserRead)
def delete_user_endpoint(user_id: str, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return delete_user(db, user)
