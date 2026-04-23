from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class SleepLogBase(ORMModel):
    daily_log_id: UUID
    sleep_start: datetime | None = None
    sleep_end: datetime | None = None
    sleep_hours: float | None = Field(default=None, ge=0, le=24)
    sleep_quality: int | None = Field(default=None, ge=1, le=5)


class SleepLogCreate(SleepLogBase):
    pass


class SleepLogUpdate(ORMModel):
    sleep_start: datetime | None = None
    sleep_end: datetime | None = None
    sleep_hours: float | None = Field(default=None, ge=0, le=24)
    sleep_quality: int | None = Field(default=None, ge=1, le=5)


class SleepLogRead(SleepLogBase):
    id: UUID
    created_at: datetime
