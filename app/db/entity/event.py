from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid


class Event(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    calendar_id: Optional[str] = Field(default=None, max_length=36)
    user_id: str = Field(max_length=36)
    task_id: Optional[str] = Field(default=None, max_length=36)
    title: str = Field(max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    start_at: datetime
    end_at: datetime
    location: Optional[str] = Field(default=None, max_length=100)
    source_type: Optional[str] = Field(default=None, max_length=20)
    created_by_agent: Optional[str] = Field(default=None, max_length=30)
    recurrence_rule: Optional[str] = Field(default=None, max_length=200)
    timezone: Optional[str] = Field(default=None, max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
