import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str | None] = mapped_column(String(150), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    daily_logs = relationship("DailyLog", back_populates="user", cascade="all, delete-orphan")


class DailyLog(Base):
    __tablename__ = "daily_logs"
    __table_args__ = (
        UniqueConstraint("user_id", "log_date", name="unique_user_log_date"),
        CheckConstraint("mood BETWEEN 1 AND 5", name="check_mood_range"),
        CheckConstraint("energy BETWEEN 1 AND 5", name="check_energy_range"),
        CheckConstraint("stress BETWEEN 1 AND 5", name="check_stress_range"),
        CheckConstraint("mental_clarity BETWEEN 1 AND 5", name="check_mental_clarity_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    log_date: Mapped[date] = mapped_column(Date, nullable=False)
    mood: Mapped[int | None] = mapped_column(Integer)
    energy: Mapped[int | None] = mapped_column(Integer)
    stress: Mapped[int | None] = mapped_column(Integer)
    mental_clarity: Mapped[int | None] = mapped_column(Integer)
    best_of_day: Mapped[str | None] = mapped_column(Text)
    worst_of_day: Mapped[str | None] = mapped_column(Text)
    main_drop_cause: Mapped[str | None] = mapped_column(Text)
    biggest_bad_decision: Mapped[str | None] = mapped_column(Text)
    notes: Mapped[str | None] = mapped_column(Text)
    daily_score: Mapped[float | None] = mapped_column(Numeric(5, 2))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="daily_logs")
    sleep_log = relationship("SleepLog", back_populates="daily_log", cascade="all, delete-orphan", uselist=False)
    study_sessions = relationship("StudySession", back_populates="daily_log", cascade="all, delete-orphan")
    workouts = relationship("Workout", back_populates="daily_log", cascade="all, delete-orphan")
    distractions = relationship("Distraction", back_populates="daily_log", cascade="all, delete-orphan")


class SleepLog(Base):
    __tablename__ = "sleep_logs"
    __table_args__ = (
        CheckConstraint("sleep_hours >= 0 AND sleep_hours <= 24", name="check_sleep_hours_range"),
        CheckConstraint("sleep_quality BETWEEN 1 AND 5", name="check_sleep_quality_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    daily_log_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("daily_logs.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    sleep_start: Mapped[datetime | None] = mapped_column(DateTime)
    sleep_end: Mapped[datetime | None] = mapped_column(DateTime)
    sleep_hours: Mapped[float | None] = mapped_column(Numeric(4, 2))
    sleep_quality: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    daily_log = relationship("DailyLog", back_populates="sleep_log")


class StudySession(Base):
    __tablename__ = "study_sessions"
    __table_args__ = (
        CheckConstraint("planned_minutes >= 0", name="check_planned_minutes_non_negative"),
        CheckConstraint("real_minutes >= 0", name="check_real_minutes_non_negative"),
        CheckConstraint("focus BETWEEN 1 AND 5", name="check_focus_range"),
        CheckConstraint("difficulty BETWEEN 1 AND 5", name="check_difficulty_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    daily_log_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("daily_logs.id", ondelete="CASCADE"), nullable=False)
    topic: Mapped[str] = mapped_column(String(150), nullable=False)
    planned_minutes: Mapped[int | None] = mapped_column(Integer)
    real_minutes: Mapped[int | None] = mapped_column(Integer)
    focus: Mapped[int | None] = mapped_column(Integer)
    difficulty: Mapped[int | None] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    daily_log = relationship("DailyLog", back_populates="study_sessions")


class Workout(Base):
    __tablename__ = "workouts"
    __table_args__ = (
        CheckConstraint("duration_minutes >= 0", name="check_duration_minutes_non_negative"),
        CheckConstraint("intensity BETWEEN 1 AND 5", name="check_intensity_range"),
        CheckConstraint("performance BETWEEN 1 AND 5", name="check_performance_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    daily_log_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("daily_logs.id", ondelete="CASCADE"), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    workout_type: Mapped[str | None] = mapped_column(String(100))
    duration_minutes: Mapped[int | None] = mapped_column(Integer)
    intensity: Mapped[int | None] = mapped_column(Integer)
    performance: Mapped[int | None] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    daily_log = relationship("DailyLog", back_populates="workouts")


class Distraction(Base):
    __tablename__ = "distractions"
    __table_args__ = (
        CheckConstraint("duration_minutes >= 0", name="check_distraction_duration_non_negative"),
        CheckConstraint("impact BETWEEN 1 AND 5", name="check_impact_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    daily_log_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("daily_logs.id", ondelete="CASCADE"), nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[datetime | None] = mapped_column(DateTime)
    duration_minutes: Mapped[int | None] = mapped_column(Integer)
    impact: Mapped[int | None] = mapped_column(Integer)
    trigger_reason: Mapped[str | None] = mapped_column(Text)
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    daily_log = relationship("DailyLog", back_populates="distractions")
