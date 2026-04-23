from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.daily_logs import router as daily_logs_router
from app.api.distractions import router as distractions_router
from app.api.sleep_logs import router as sleep_logs_router
from app.api.study_sessions import router as study_sessions_router
from app.api.users import router as users_router
from app.api.workouts import router as workouts_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Performance Tracker API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(users_router, prefix="/api/v1")
app.include_router(daily_logs_router, prefix="/api/v1")
app.include_router(sleep_logs_router, prefix="/api/v1")
app.include_router(study_sessions_router, prefix="/api/v1")
app.include_router(workouts_router, prefix="/api/v1")
app.include_router(distractions_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
