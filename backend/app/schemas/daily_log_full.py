from datetime import date, datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel
from app.schemas.daily_log import DailyLogRead
from app.schemas.distraction import DistractionRead
from app.schemas.sleep_log import SleepLogRead
from app.schemas.study_session import StudySessionRead
from app.schemas.workout import WorkoutRead


class SleepLogNestedCreate(ORMModel):
    sleep_start: datetime | None = None
    sleep_end: datetime | None = None
    sleep_hours: float | None = Field(default=None, ge=0, le=24)
    sleep_quality: int | None = Field(default=None, ge=1, le=5)


class StudySessionNestedCreate(ORMModel):
    topic: str = Field(min_length=1, max_length=150)
    planned_minutes: int | None = Field(default=None, ge=0)
    real_minutes: int | None = Field(default=None, ge=0)
    focus: int | None = Field(default=None, ge=1, le=5)
    difficulty: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class WorkoutNestedCreate(ORMModel):
    done: bool = False
    workout_type: str | None = Field(default=None, max_length=100)
    duration_minutes: int | None = Field(default=None, ge=0)
    intensity: int | None = Field(default=None, ge=1, le=5)
    performance: int | None = Field(default=None, ge=1, le=5)
    notes: str | None = None


class DistractionNestedCreate(ORMModel):
    type: str = Field(min_length=1, max_length=100)
    start_time: datetime | None = None
    duration_minutes: int | None = Field(default=None, ge=0)
    impact: int | None = Field(default=None, ge=1, le=5)
    trigger_reason: str | None = None
    notes: str | None = None


class DailyLogFullCreate(ORMModel):
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

    sleep_log: SleepLogNestedCreate | None = None
    study_sessions: list[StudySessionNestedCreate] = Field(default_factory=list)
    workouts: list[WorkoutNestedCreate] = Field(default_factory=list)
    distractions: list[DistractionNestedCreate] = Field(default_factory=list)


class DailyLogFullRead(ORMModel):
    daily_log: DailyLogRead
    sleep_log: SleepLogRead | None
    study_sessions: list[StudySessionRead]
    workouts: list[WorkoutRead]
    distractions: list[DistractionRead]
