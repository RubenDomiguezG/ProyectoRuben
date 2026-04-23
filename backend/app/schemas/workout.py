from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class WorkoutBase(ORMModel):
    daily_log_id: UUID
    done: bool = False
    workout_type: str | None = Field(default=None, max_length=100)
    duration_minutes: int | None = Field(default=None, ge=0)
    intensity: int | None = Field(default=None, ge=1, le=5)
    performance: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutUpdate(ORMModel):
    done: bool | None = None
    workout_type: str | None = Field(default=None, max_length=100)
    duration_minutes: int | None = Field(default=None, ge=0)
    intensity: int | None = Field(default=None, ge=1, le=5)
    performance: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class WorkoutRead(WorkoutBase):
    id: UUID
    created_at: datetime
