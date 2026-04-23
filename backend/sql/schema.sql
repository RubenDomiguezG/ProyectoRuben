CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE daily_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    log_date DATE NOT NULL,
    mood SMALLINT CHECK (mood BETWEEN 1 AND 5),
    energy SMALLINT CHECK (energy BETWEEN 1 AND 5),
    stress SMALLINT CHECK (stress BETWEEN 1 AND 5),
    mental_clarity SMALLINT CHECK (mental_clarity BETWEEN 1 AND 5),
    best_of_day TEXT,
    worst_of_day TEXT,
    main_drop_cause TEXT,
    biggest_bad_decision TEXT,
    notes TEXT,
    daily_score NUMERIC(5,2),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT unique_user_log_date UNIQUE (user_id, log_date)
);

CREATE TABLE sleep_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    daily_log_id UUID NOT NULL UNIQUE REFERENCES daily_logs(id) ON DELETE CASCADE,
    sleep_start TIMESTAMP,
    sleep_end TIMESTAMP,
    sleep_hours NUMERIC(4,2) CHECK (sleep_hours >= 0 AND sleep_hours <= 24),
    sleep_quality SMALLINT CHECK (sleep_quality BETWEEN 1 AND 5),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE study_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    daily_log_id UUID NOT NULL REFERENCES daily_logs(id) ON DELETE CASCADE,
    topic VARCHAR(150) NOT NULL,
    planned_minutes INTEGER CHECK (planned_minutes >= 0),
    real_minutes INTEGER CHECK (real_minutes >= 0),
    focus SMALLINT CHECK (focus BETWEEN 1 AND 5),
    difficulty SMALLINT CHECK (difficulty BETWEEN 1 AND 5),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE workouts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    daily_log_id UUID NOT NULL REFERENCES daily_logs(id) ON DELETE CASCADE,
    done BOOLEAN NOT NULL DEFAULT FALSE,
    workout_type VARCHAR(100),
    duration_minutes INTEGER CHECK (duration_minutes >= 0),
    intensity SMALLINT CHECK (intensity BETWEEN 1 AND 5),
    performance SMALLINT CHECK (performance BETWEEN 1 AND 5),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE distractions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    daily_log_id UUID NOT NULL REFERENCES daily_logs(id) ON DELETE CASCADE,
    type VARCHAR(100) NOT NULL,
    start_time TIMESTAMP,
    duration_minutes INTEGER CHECK (duration_minutes >= 0),
    impact SMALLINT CHECK (impact BETWEEN 1 AND 5),
    trigger_reason TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_daily_logs_user_id ON daily_logs(user_id);
CREATE INDEX idx_daily_logs_log_date ON daily_logs(log_date);
CREATE INDEX idx_study_sessions_daily_log_id ON study_sessions(daily_log_id);
CREATE INDEX idx_workouts_daily_log_id ON workouts(daily_log_id);
CREATE INDEX idx_distractions_daily_log_id ON distractions(daily_log_id);
