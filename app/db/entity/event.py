from sqlmodel import SQLModel, Field
from typing import Optional
import uuid
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone

class Event(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    calendar_id: Optional[str] = Field(default=None, max_length=36)
    user_id: str = Field(max_length=36)
    task_id: Optional[str] = Field(default=None, max_length=36)
    title: str = Field(max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    start_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True))  # Use timezone-aware
    )
    end_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True))
    )
    location: Optional[str] = Field(default=None, max_length=100)
    source_type: Optional[str] = Field(default=None, max_length=20)
    created_by_agent: Optional[str] = Field(default=None, max_length=30)
    recurrence_rule: Optional[str] = Field(default=None, max_length=200)
    timezone: Optional[str] = Field(default=None, max_length=50)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True))  # Use timezone-aware
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True))
    )
