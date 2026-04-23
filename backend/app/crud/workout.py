from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import Workout
from app.schemas.workout import WorkoutCreate, WorkoutUpdate


def list_workouts(db: Session):
    return list_all(db, Workout)


def get_workout(db: Session, item_id: str):
    return get_one(db, Workout, item_id)


def create_workout(db: Session, payload: WorkoutCreate):
    return create_one(db, Workout, payload)


def update_workout(db: Session, item: Workout, payload: WorkoutUpdate):
    return update_one(db, item, payload)


def delete_workout(db: Session, item: Workout):
    return delete_one(db, item)
