from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class DistractionBase(ORMModel):
    daily_log_id: UUID
    type: str = Field(min_length=1, max_length=100)
    start_time: datetime | None = None
    duration_minutes: int | None = Field(default=None, ge=0)
    impact: int | None = Field(default=None, ge=1, le=5)
    trigger_reason: str | None = None
    notes: str | None = None


class DistractionCreate(DistractionBase):
    pass


class DistractionUpdate(ORMModel):
    type: str | None = Field(default=None, min_length=1, max_length=100)
    start_time: datetime | None = None
    duration_minutes: int | None = Field(default=None, ge=0)
    impact: int | None = Field(default=None, ge=1, le=5)
    trigger_reason: str | None = None
    notes: str | None = None


class DistractionRead(DistractionBase):
    id: UUID
    created_at: datetime
