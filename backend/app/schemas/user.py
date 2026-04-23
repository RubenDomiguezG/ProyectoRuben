from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.common import ORMModel


class UserBase(ORMModel):
    name: str = Field(min_length=1, max_length=100)
    email: str | None = Field(default=None, max_length=150)


class UserCreate(UserBase):
    pass


class UserUpdate(ORMModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: str | None = Field(default=None, max_length=150)


class UserRead(UserBase):
    id: UUID
    created_at: datetime
