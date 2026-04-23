from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.workout import create_workout, delete_workout, get_workout, list_workouts, update_workout
from app.db.session import get_db
from app.schemas.workout import WorkoutCreate, WorkoutRead, WorkoutUpdate

router = APIRouter(prefix="/workouts", tags=["workouts"])


@router.get("/", response_model=list[WorkoutRead])
def list_workouts_endpoint(db: Session = Depends(get_db)):
    return list_workouts(db)


@router.get("/{item_id}", response_model=WorkoutRead)
def get_workout_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_workout(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    return item


@router.post("/", response_model=WorkoutRead, status_code=status.HTTP_201_CREATED)
def create_workout_endpoint(payload: WorkoutCreate, db: Session = Depends(get_db)):
    return create_workout(db, payload)


@router.put("/{item_id}", response_model=WorkoutRead)
def update_workout_endpoint(item_id: str, payload: WorkoutUpdate, db: Session = Depends(get_db)):
    item = get_workout(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    return update_workout(db, item, payload)


@router.delete("/{item_id}", response_model=WorkoutRead)
def delete_workout_endpoint(item_id: str, db: Session = Depends(get_db)):
    item = get_workout(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    return delete_workout(db, item)
