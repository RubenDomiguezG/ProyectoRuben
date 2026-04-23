from datetime import date, datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class DailyLogBase(ORMModel):
    user_id: UUID
    log_date: date
    mood: int | None = Field(default=None, ge=1, le=5)
    energy: int | None = Field(default=None, ge=1, le=5)
    stress: int | None = Field(default=None, ge=1, le=5)
    mental_clarity: int | None = Field(default=None, ge=1, le=5)
    best_of_day: str | None = None
    worst_of_day: str | None = None
    main_drop_cause: str | None = None
    biggest_bad_decision: str | None = None
    notes: str | None = None
    daily_score: float | None = Field(default=None, ge=0, le=100)


class DailyLogCreate(DailyLogBase):
    pass


class DailyLogUpdate(ORMModel):
    mood: int | None = Field(default=None, ge=1, le=5)
    energy: int | None = Field(default=None, ge=1, le=5)
    stress: int | None = Field(default=None, ge=1, le=5)
    mental_clarity: int | None = Field(default=None, ge=1, le=5)
    best_of_day: str | None = None
    worst_of_day: str | None = None
    main_drop_cause: str | None = None
    biggest_bad_decision: str | None = None
    notes: str | None = None
    daily_score: float | None = Field(default=None, ge=0, le=100)


class DailyLogRead(DailyLogBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
