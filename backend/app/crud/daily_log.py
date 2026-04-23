from datetime import date

from sqlalchemy.orm import Session, joinedload

from app.crud.common import create_one, delete_one, get_one, update_one
from app.models.models import DailyLog, Distraction, SleepLog, StudySession, Workout
from app.schemas.daily_log import DailyLogCreate, DailyLogUpdate
from app.schemas.daily_log_full import DailyLogFullCreate


def list_daily_logs(db: Session):
    return db.query(DailyLog).order_by(DailyLog.log_date.desc()).all()


def get_daily_log(db: Session, log_id: str):
    return get_one(db, DailyLog, log_id)


def get_daily_log_full_by_id(db: Session, log_id: str):
    return (
        db.query(DailyLog)
        .options(
            joinedload(DailyLog.sleep_log),
            joinedload(DailyLog.study_sessions),
            joinedload(DailyLog.workouts),
            joinedload(DailyLog.distractions),
        )
        .filter(DailyLog.id == log_id)
        .first()
    )


def get_daily_log_full_by_date(db: Session, log_date: date):
    return (
        db.query(DailyLog)
        .options(
            joinedload(DailyLog.sleep_log),
            joinedload(DailyLog.study_sessions),
            joinedload(DailyLog.workouts),
            joinedload(DailyLog.distractions),
        )
        .filter(DailyLog.log_date == log_date)
        .first()
    )


def create_daily_log(db: Session, payload: DailyLogCreate):
    return create_one(db, DailyLog, payload)


def create_daily_log_full(db: Session, payload: DailyLogFullCreate):
    daily_log = DailyLog(
        user_id=payload.user_id,
        log_date=payload.log_date,
        mood=payload.mood,
        energy=payload.energy,
        stress=payload.stress,
        mental_clarity=payload.mental_clarity,
        best_of_day=payload.best_of_day,
        worst_of_day=payload.worst_of_day,
        main_drop_cause=payload.main_drop_cause,
        biggest_bad_decision=payload.biggest_bad_decision,
        notes=payload.notes,
        daily_score=payload.daily_score,
    )
    db.add(daily_log)
    db.flush()

    if payload.sleep_log:
        db.add(
            SleepLog(
                daily_log_id=daily_log.id,
                sleep_start=payload.sleep_log.sleep_start,
                sleep_end=payload.sleep_log.sleep_end,
                sleep_hours=payload.sleep_log.sleep_hours,
                sleep_quality=payload.sleep_log.sleep_quality,
            )
        )

    for session in payload.study_sessions:
        db.add(
            StudySession(
                daily_log_id=daily_log.id,
                topic=session.topic,
                planned_minutes=session.planned_minutes,
                real_minutes=session.real_minutes,
                focus=session.focus,
                difficulty=session.difficulty,
                notes=session.notes,
            )
        )

    for workout in payload.workouts:
        db.add(
            Workout(
                daily_log_id=daily_log.id,
                done=workout.done,
                workout_type=workout.workout_type,
                duration_minutes=workout.duration_minutes,
                intensity=workout.intensity,
                performance=workout.performance,
                notes=workout.notes,
            )
        )

    for distraction in payload.distractions:
        db.add(
            Distraction(
                daily_log_id=daily_log.id,
                type=distraction.type,
                start_time=distraction.start_time,
                duration_minutes=distraction.duration_minutes,
                impact=distraction.impact,
                trigger_reason=distraction.trigger_reason,
                notes=distraction.notes,
            )
        )

    db.commit()
    return get_daily_log_full_by_id(db, str(daily_log.id))


def update_daily_log(db: Session, daily_log: DailyLog, payload: DailyLogUpdate):
    return update_one(db, daily_log, payload)


def delete_daily_log(db: Session, daily_log: DailyLog):
    return delete_one(db, daily_log)
