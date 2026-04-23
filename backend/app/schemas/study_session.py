from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class StudySessionBase(ORMModel):
    daily_log_id: UUID
    topic: str = Field(min_length=1, max_length=150)
    planned_minutes: int | None = Field(default=None, ge=0)
    real_minutes: int | None = Field(default=None, ge=0)
    focus: int | None = Field(default=None, ge=1, le=5)
    difficulty: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class StudySessionCreate(StudySessionBase):
    pass


class StudySessionUpdate(ORMModel):
    topic: str | None = Field(default=None, min_length=1, max_length=150)
    planned_minutes: int | None = Field(default=None, ge=0)
    real_minutes: int | None = Field(default=None, ge=0)
    focus: int | None = Field(default=None, ge=1, le=5)
    difficulty: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class StudySessionRead(StudySessionBase):
    id: UUID
    created_at: datetime
