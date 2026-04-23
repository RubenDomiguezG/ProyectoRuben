from sqlalchemy.orm import Session

from app.crud.common import create_one, delete_one, get_one, list_all, update_one
from app.models.models import StudySession
from app.schemas.study_session import StudySessionCreate, StudySessionUpdate


def list_study_sessions(db: Session):
    return list_all(db, StudySession)


def get_study_session(db: Session, item_id: str):
    return get_one(db, StudySession, item_id)


def create_study_session(db: Session, payload: StudySessionCreate):
    return create_one(db, StudySession, payload)


def update_study_session(db: Session, item: StudySession, payload: StudySessionUpdate):
    return update_one(db, item, payload)


def delete_study_session(db: Session, item: StudySession):
    return delete_one(db, item)
